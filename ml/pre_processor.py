import re
from config import Config
from core.tools import tls


class Preprocessor():
    def deEmojify(
        slef,
        text: str
    ) -> str:

        regrex_pattern = re.compile(pattern="["
                                    u"\U0001F600-\U0001F64F"  # emoticons
                                    u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                                    u"\U0001F680-\U0001F6FF"  # transport & map symbols
                                    u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                                    "]+", flags=re.UNICODE)
        text = regrex_pattern.sub(r'', text)
        if Config.REMOVE_NUMBER:
            text = re.sub(r'\d+', '', text)
        return text

    def prepare_data(self):
        pre_trainin_text: list = []
        fine_tuning_text: list = []

        tls.log('Corpus pre-processing...', bold=True)
        corpus_fine_tuning_full_path: str = Config.FINE_TUNING_CORPUS_PATH + \
            Config.FINE_TUNING_FILENAME

        corpus_pre_training_full_path: str = Config.PRE_TRAINING_CORPUS_PATH + \
            Config.PRE_TRAINING_FILENAME

        # read files
        with open(corpus_pre_training_full_path, encoding='utf8') as f:
            for line in f:
                if type(line) is str:
                    pre_trainin_text.append(self.deEmojify(line.strip()))

        with open(corpus_fine_tuning_full_path, encoding='utf8') as f:
            for line in f:
                if type(line) is str:
                    fine_tuning_text.append(self.deEmojify(line.strip()))

        with open(corpus_fine_tuning_full_path, "w", encoding='utf-8') as txt_file:
            for line in fine_tuning_text:
                txt_file.write("".join(line) + "\n")

        tls.log(f'Pre-processed {Config.FINE_TUNING_FILENAME} saved in corpus.')

        # write processed files
        with open(corpus_pre_training_full_path, "w", encoding='utf-8') as txt_file:
            for line in pre_trainin_text:
                txt_file.write("".join(line) + "\n")
                
        tls.log(f'Pre-processed {Config.PRE_TRAINING_FILENAME} saved in corpus.')
