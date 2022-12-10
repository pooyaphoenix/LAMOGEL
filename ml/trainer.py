
import time
from transformers import BertTokenizer, BertForMaskedLM
from torch import flatten, save, cuda, rand, device
from torch.utils.data import DataLoader
from transformers import AdamW
from tqdm import tqdm

from config import Config
from core.tools import tls
from domain.custom_dataset import CustomDataset


class MlmTrainer():
    def __init__(self) -> None:
        tls.log('Loading Model and Tokenizer ...', bold=True)
        self.tokenizer = BertTokenizer.from_pretrained(Config.TOKENIZER_MODEL)
        self.model = BertForMaskedLM.from_pretrained(Config.PRE_TRAINED_MODEL)

    def tokenize_input(self) -> CustomDataset(list):
        # read files
        corpus: list = []
        corpus_pre_training_full_path: str = Config.PRE_TRAINING_CORPUS_PATH + \
            Config.PRE_TRAINING_FILENAME

        with open(corpus_pre_training_full_path, encoding='utf8') as f:
            for line in f:
                corpus.append(line)

        inputs = self.tokenizer(corpus,
                                return_tensors='pt',
                                max_length=Config.TOKENIZER_MAX_LENGTH,
                                truncation=True,
                                padding='max_length'
                                )

        inputs['labels'] = inputs.input_ids.detach().clone()
        
        rand_ = rand(inputs.input_ids.shape)
        # create mask array
        mask_arr = (rand_ < Config.MASK_CONFIDENCE) * (inputs.input_ids != 101) * \
            (inputs.input_ids != 102) * (inputs.input_ids != 0)
        selection = []
        for i in range(inputs.input_ids.shape[0]):
            selection.append(
                flatten(mask_arr[i].nonzero()).tolist()
            )
        for i in range(inputs.input_ids.shape[0]):
            inputs.input_ids[i, selection[i]] = 103

        return CustomDataset(inputs)

    def trainer(self, device, data_loader):
        tls.log('Trainer started ...', bold=True)

        optimizer = AdamW(self.model.parameters(), lr=Config.LR)

        epochs = Config.EPOCHS

        for epoch in range(epochs):
            # setup loop with TQDM and dataloader
            loop = tqdm(data_loader, leave=True)

            for batch in loop:
                # initialize calculated gradients (from prev step)
                optimizer.zero_grad()
                # pull all tensor batches required for training
                input_ids = batch['input_ids'].to(device)
                #
                attention_mask = batch['attention_mask'].to(device)
                #
                labels = batch['labels'].to(device)
                # process
                outputs = self.model(input_ids, attention_mask=attention_mask,
                                     labels=labels)
                # extract loss
                loss = outputs.loss
                # calculate loss for every parameter that needs grad update
                loss.backward()
                # update parameters
                optimizer.step()
                # print relevant info to progress bar
                loop.set_description(f'Epoch {epoch}')
                loop.set_postfix(loss=loss.item())

    def get_device(self) -> any:
        device_ = device('cuda') if cuda.is_available() else device('cpu')
        tls.log(f"[Model running on {device_}]", bold=True)
        return device_

    def start(self):
        # tokenized data
        tokenized_data = self.tokenize_input()

        # load data to data loader
        data_loader = DataLoader(
            tokenized_data, batch_size=Config.BATCH_SIZE, shuffle=True)

        # get divice from cuda (gpu or cpu)
        device = self.get_device()

        # move our model over to the selected device
        self.model.to(device)

        # activate training mode
        self.model.train()

        # do train
        self.trainer(device, data_loader)

        # make model path file
        model_file_path: str = (Config.GENERATED_MODEL_PATH +
                                Config.GENERATED_MODEL_NAME + '-' +
                                time.strftime("%Y%m%d-%H%M%S") +
                                Config.GENERATED_MODEL_FORMAT)

        # save model
        save(self.model.state_dict(), model_file_path)

        tls.log(f"Model saved in {model_file_path}", bold=True)
