from db.chat_session_handler import ChatSessionHandler
from data_handler import DataHandler
from config import Config
from ml.pre_processor import Preprocessor
from ml.trainer import MlmTrainer

if __name__== "__main__":

    dh = DataHandler()
    data = dh.split_data()

    preprocessor = Preprocessor()
    preprocessor.prepare_data()

    mlm_trainer = MlmTrainer()
    mlm_trainer.start()