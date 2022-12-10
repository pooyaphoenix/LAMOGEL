from math import ceil
from random import shuffle

from db.chat_session_repo import ChatSessionRepo
from config import Config
from core.tools import tls


class DataHandler():
    def save_data_into_corpus_files(
        self,
        fine_tuning_data: list = [],
        pre_trainin_data: list = []
    ):
        corpus_fine_tuning_full_path: str = Config.FINE_TUNING_CORPUS_PATH + \
            Config.FINE_TUNING_FILENAME
        corpus_pre_training_full_path: str = Config.PRE_TRAINING_CORPUS_PATH + \
            Config.PRE_TRAINING_FILENAME

        with open(corpus_fine_tuning_full_path, "w", encoding='utf-8') as txt_file:
            for line in fine_tuning_data:
                txt_file.write(" ".join(line) + "\n")
            tls.log(f'{Config.FINE_TUNING_FILENAME} saved in corpus.')

        with open(corpus_pre_training_full_path, "w", encoding='utf-8') as txt_file:
            for line in pre_trainin_data:
                txt_file.write(" ".join(line) + "\n")
            tls.log(f'{Config.PRE_TRAINING_FILENAME} saved in corpus.')

    def split_data(
        self,
        split_range: int = Config.SPLIT_RANGE,
        shuffling: bool = Config.IS_SHUFFLE
    ) -> dict:
        message_list: list = ChatSessionRepo().get_all()

        if len(message_list) == 0:
            return None
            
        if shuffling:
            shuffle(message_list)

        split_index: int = int(ceil((split_range*len(message_list))))
        fine_tuning_data: list = message_list[:split_index]
        pre_trainin_data: list = message_list[split_index:]

        self.save_data_into_corpus_files(fine_tuning_data, pre_trainin_data)

        result_dict: dict = {
            "fine_tuning": fine_tuning_data,
            "pre_traning": pre_trainin_data,
            "full_len": len(message_list),
            "fine_tuning_len": len(fine_tuning_data),
            "pre_traning_len": len(pre_trainin_data)
        }

        tls.log('Files details: ', bold=True)
        tls.log(
            f"total records: {len(message_list)} \nfine_tuning records:{len(fine_tuning_data)}  \npre_traning records:{len(pre_trainin_data)}",
            bold=True)

        return result_dict
