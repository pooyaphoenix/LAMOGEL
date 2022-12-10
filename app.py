from core.data_handler import DataHandler
from ml.pre_processor import Preprocessor
from ml.trainer import MlmTrainer


if __name__== "__main__":

    # split data between fine-tuning and pre-training data
    DataHandler().split_data()

    # require pre-processing techniques on spiltted data
    Preprocessor().prepare_data()

    #run MLM trainer class to export language model  
    MlmTrainer().start()