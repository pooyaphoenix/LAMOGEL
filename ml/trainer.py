
from transformers import BertTokenizer, BertForMaskedLM
import torch
from config import Config
from kernel.color import color
from tqdm import tqdm 
from transformers import AdamW


class CustomDataset(torch.utils.data.Dataset):
    def __init__(self, encodings):
        self.encodings = encodings
    def __getitem__(self, idx):
        return {key: torch.tensor(val[idx]) for key, val in self.encodings.items()}
    def __len__(self):
        return len(self.encodings.input_ids)


class MlmTrainer():
    def __init__(self) -> None:
        print(color.BOLD + color.BLUE + 'Loading Model and Tokenizer ...'+ color.END)
        self.tokenizer = BertTokenizer.from_pretrained(Config.tokenizer)
        self.model = BertForMaskedLM.from_pretrained(Config.pre_trained_model)

    def make_input(self) -> list:
         #read files
        corpus: list = []
        with open(Config.pre_training_curpus_path + Config.pre_training_file_name, encoding='utf8') as f:
            for line in f:
                    corpus.append(line)

        inputs = self.tokenizer(corpus, return_tensors='pt', max_length=100, truncation=True, padding='max_length')
        inputs['labels'] = inputs.input_ids.detach().clone()
        rand = torch.rand(inputs.input_ids.shape)
        # create mask array
        mask_arr = (rand < 0.15) * (inputs.input_ids != 101) * \
                (inputs.input_ids != 102) * (inputs.input_ids != 0)
        selection = []
        for i in range(inputs.input_ids.shape[0]):
            selection.append(
                torch.flatten(mask_arr[i].nonzero()).tolist()
            )
        for i in range(inputs.input_ids.shape[0]):
            inputs.input_ids[i, selection[i]] = 103

        return inputs


    def trainer(self, device, data_loader):
        optim = AdamW(self.model.parameters(), lr=5e-5)
        epochs = 1
        for epoch in range(epochs):
            # setup loop with TQDM and dataloader
            loop = tqdm(data_loader, leave=True)
            for batch in loop:
                # initialize calculated gradients (from prev step)
                optim.zero_grad()
                # pull all tensor batches required for training
                input_ids = batch['input_ids'].to(device)
                attention_mask = batch['attention_mask'].to(device)
                labels = batch['labels'].to(device)
                # process
                outputs = self.model(input_ids, attention_mask=attention_mask,
                                labels=labels)
                # extract loss
                loss = outputs.loss
                # calculate loss for every parameter that needs grad update
                loss.backward()
                # update parameters
                optim.step()
                # print relevant info to progress bar
                loop.set_description(f'Epoch {epoch}')
                loop.set_postfix(loss=loss.item())

    def start(self):

        dataset = CustomDataset(self.make_input())
        data_loader = torch.utils.data.DataLoader(dataset, batch_size=4, shuffle=True)

        device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
        print(f"device on {device}")
        # and move our model over to the selected device
        self.model.to(device)
        # activate training mode
        self.model.train()
        self.trainer(device, data_loader)
        torch.save(self.model.state_dict(), 'azki_bert.pt')
        
        return 'successful.'



