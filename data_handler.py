from db.chat_session_handler import ChatSessionHandler
from random import shuffle
import math
from kernel.color import color
from config import Config
class DataHandler():

    def __init__(self) -> None:
        self.chat_session = ChatSessionHandler()

    def save_data_corpus(
                self,
                fine_tuning_data: list = [],
                pre_trainin_data: list = []
    ):

        with open(Config.fine_tuning_curpus_path + Config.fine_tuning_file_name, "w", encoding='utf-8') as txt_file:
            for line in fine_tuning_data:
                txt_file.write(" ".join(line) + "\n") 
            print(f'{Config.fine_tuning_file_name} saved in corpus.')

        with open(Config.pre_training_curpus_path + Config.pre_training_file_name, "w", encoding='utf-8') as txt_file:
            for line in pre_trainin_data:
                txt_file.write(" ".join(line) + "\n") 
            print(f'{Config.pre_training_file_name} saved in corpus.')


    def split_data(
            self, 
            split_range: int = Config.split_range, 
            shuffle_status: bool = Config.shuffle_status
        ) -> dict:
        data: list = self.chat_session.get_all()

        if shuffle_status:
            shuffle(data)

        split_idx: int = int(math.ceil((split_range*len(data))))
        fine_tuning_data:list = data [:split_idx]
        pre_trainin_data:list = data [split_idx:]

        self.save_data_corpus(fine_tuning_data, pre_trainin_data)
        result_dict :dict = {
            "fine_tuning": fine_tuning_data,
            "pre_traning": pre_trainin_data,
            "len": len(data),
            "f_len":len(fine_tuning_data),
            "p_len":len(pre_trainin_data)
        }
        print(color.BOLD + color.BLUE + 'files details'+ color.END)
        print(f"total records: {len(data)} \nfine_tuning records:{len(fine_tuning_data)}  \npre_traning records:{len(pre_trainin_data)}")
        return result_dict






