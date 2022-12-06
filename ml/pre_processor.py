import re
from config import Config
from data_handler import DataHandler
from kernel.color import color

class Preprocessor():

    def __init__(self) -> None:
        pass
    def deEmojify(
                slef,
                text:str =''
        ) -> str:

        regrex_pattern = re.compile(pattern = "["
            u"\U0001F600-\U0001F64F"  # emoticons
            u"\U0001F300-\U0001F5FF"  # symbols & pictographs
            u"\U0001F680-\U0001F6FF"  # transport & map symbols
            u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                            "]+", flags = re.UNICODE)
        text = regrex_pattern.sub(r'',text)
        if Config.remove_number:
            text = re.sub(r'\d+', '', text)
        return text

    def prepare_data(self):
        
        p_text :list = []
        f_text :list = []
        print(color.BOLD + color.BLUE + 'corpus pre-processing...'+ color.END)

        #read files
        with open(Config.pre_training_curpus_path + Config.pre_training_file_name, encoding='utf8') as f:
            for line in f:
                if type(line) is str:
                    p_text.append(self.deEmojify(line.strip()))

        with open(Config.fine_tuning_curpus_path + Config.fine_tuning_file_name, encoding='utf8') as f:
            for line in f:
                if type(line) is str:
                    f_text.append(self.deEmojify(line.strip()))


        with open(Config.fine_tuning_curpus_path + Config.fine_tuning_file_name, "w", encoding='utf-8') as txt_file:
            for line in f_text:
                txt_file.write("".join(line) + "\n") 
            print(f'pre-processed {Config.fine_tuning_file_name} saved in corpus.')

        #write processed files
        with open(Config.pre_training_curpus_path + Config.pre_training_file_name, "w", encoding='utf-8') as txt_file:
            for line in p_text:
                txt_file.write("".join(line) + "\n") 
            print(f'pre-processed {Config.pre_training_file_name} saved in corpus.')


        
