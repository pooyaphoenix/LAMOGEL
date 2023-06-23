from core.data_handler import DataHandler
from ml.pre_processor import Preprocessor
from ml.trainer import MlmTrainer
from ml.hugging_face import HuggingFace

if __name__== "__main__":

    # split data between fine-tuning and pre-training data
    DataHandler().split_data()

    # require pre-processing techniques on spiltted data
    Preprocessor().prepare_data()

    # #run MLM trainer class to export language model  
    MlmTrainer().start()

    # push language model to hugging-face.co 
    
    # hugging_face = HuggingFace()
    # repo, origin = hugging_face.set_up_to_date_with_remote()
    # hugging_face.push_to_hugging_face(repo, origin)