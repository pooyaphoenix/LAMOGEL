
class Config():
    """
    All you need to customize lifecycle values is to set bottom variables values
    After the variables change you should run main.py

    """

    DEBUG_MODE: bool=True

    # curpus 
    FINE_TUNING_CORPUS_PATH: str = "data/corpus/fine_tuning/"
    PRE_TRAINING_CORPUS_PATH: str = "data/corpus/pre_training/"

    FINE_TUNING_FILENAME:str = "fine_tuning_corpus.txt"
    PRE_TRAINING_FILENAME:str = "pre_training_corpus.txt"

    #split
    SPLIT_RANGE: float = 0.995      # 1 means all data to fine-tuning and 0 means all data to pre-training (pre-training data using to mlm model)
    IS_SHUFFLE: bool = True     # shuffle returned fine-tuning and pre-training data

    #pre-processing
    REMOVE_NUMBER: bool = False

    #model and tokenizzer
    PRE_TRAINED_MODEL: str = "HooshvareLab/bert-base-parsbert-uncased"
    TOKENIZER_MODEL: str = "HooshvareLab/bert-base-parsbert-uncased"
    
    TOKENIZER_MAX_LENGTH = 100                                                 
    EPOCHS: int = 1
    BATCH_SIZE: int = 8
    MASK_CONFIDENCE: float = 0.15
    LR: float = 5e-5
    GENERATED_MODEL_PATH: str = "data/models/"
    GENERATED_MODEL_NAME: str = "azki"
    GENERATED_MODEL_FORMAT: str = ".pt"


    #database
    DB: dict = {
        
        'USER': 'pooya',
        'PASSWORD': 'kFBfBmBXRMBA',
        'ADDRESS': '172.21.30.21',
        'PORT': '30799',
        'DB_NAME': 'dev_data'
    }


   
  



