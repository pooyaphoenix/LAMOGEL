
class Config():
    """
    All you need to customize lifecycle values is to set bottom variables values
    After the variables change you should run main.py

    """

    # curpus 
    fine_tuning_curpus_path: str = "ml/corpus/fine_tuning/"
    pre_training_curpus_path: str = "ml/corpus/pre_training/"

    fine_tuning_file_name:str = "fine_tuning_corpus.txt"
    pre_training_file_name:str = "pre_training_corpus.txt"

    #split
    split_range: int = 0.99         # 1 means all data to fine-tuning and 0 means all data to pre-training (pre-training data using to mlm model)
    shuffle_status: bool = True     # shuffle returned fine-tuning and pre-training data

    #pre-processing
    remove_number: bool = False

    #model and tokenizzer
    pre_trained_model: str = "HooshvareLab/bert-base-parsbert-uncased"
    tokenizer: str = "HooshvareLab/bert-base-parsbert-uncased"
    
    tokenizer_max_length = 100                                                 
    epochs: int = 1
    batch_size: int = 4
    mask_confidence: float = 0.15
    lr = 5e-5
    generated_model_path: str = "ml/models/"
    generated_model_name: str = "azki"
    generated_model_format: str = ".pt"


    #database
    db: dict = {
        
        'USER': 'pooya',
        'PASSWORD': 'kFBfBmBXRMBA',
        'ADDRESS': '172.21.30.21',
        'PORT': '30799',
        'DB_NAME': 'dev_data'
    }


   
  



