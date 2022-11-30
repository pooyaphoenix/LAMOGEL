from db.chat_session_handler import ChatSessionHandler
from random import shuffle
import math

class DataHandler():
    def __init__(self) -> None:
        self.chat_session = ChatSessionHandler()


    def split_data(
            self, 
            split_range: int = 0.1, 
            shuffle_status: bool = True
        ) -> list:
        data: list = self.chat_session.get_all()
        print(f"({len(data)} records loaded)")

        if shuffle_status:
            shuffle(data)
        split_idx: int = int(math.ceil((split_range*len(data))))
        fine_tuning_data:list = data [:split_idx]
        pre_trainin_data:list = data [split_idx:]
        result_dict :dict = {
            "fine_tuning": fine_tuning_data,
            "pre_traning": pre_trainin_data
        }
        return result_dict


