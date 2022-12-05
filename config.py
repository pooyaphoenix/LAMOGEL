class Config():
    # curpus 
    fine_tuning_curpus_path: str = 'ml/corpus/fine_tuning/'
    pre_training_curpus_path: str = 'ml/corpus/pre_training/'

    #split
    split_range: int = 0.9         # 1 means all data to fine-tuning and 0 means all data to pre-training
    shuffle_status: bool = True   # shuffle returned fine-tuning and pre-training data

    #db
    db: dict = {

        'USER': 'root',
        'PASSWORD': '',
        'ADDRESS': 'localhost',
        'PORT': '3306',
        'DB_NAME': 'azki'
    }
  
    # USER = 'pooya'
    # PASSWORD = 'kFBfBmBXRMBA'
    # ADDRESS = '172.21.30.21'
    # PORT = '30799'
    # DB_NAME ='dev_data'
    


