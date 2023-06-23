
  # LAMOGEL: Language Model Generation Lifecycle 📝  
 LAMOGEL for the automated pre-train and fine-tuning of language model generation .
 
 LAMOGEL was implemented to connect to the database to get the data related to the NLP task and then run the Masked Language Model to build the language model and finally put the project into the Huggingface repository.
  ## Get Started 🚀  
Get Started by config: Config.py file contains the parameters and hyperparameters required for project implementation. 
Each of the parameters is categorized in this file. The mentioned hyperparameters are set in the default value for the learning model. The SPLIT_RANGE parameter is the amount of data splitting for Pre-train and fine-tuning. The closer this number is to 1, the more Fine-Tune data is.
run by app.py file
~~~bash  
  python app.py
~~~
    # split data between fine-tuning and pre-training data
    DataHandler().split_data()

    # require pre-processing techniques on spiltted data
    Preprocessor().prepare_data()

    # #run MLM trainer class to export language model  
    MlmTrainer().start()

  ## Database 🗃️  
  The specifications required for the database are in the Config file in the DB dictionary.
      
  ## Core Directory 🥝  
  The Data_handler.py file in this directory is responsible for dividing data for Pre-train and fine-tuning. The rest of the file is for managing outputs and displaying the system.

  ## Ml Directory 🦾
  • trainer.py, there is a class called MlmTrainer, which is the core of building a language model for input data. The entry point of this method is the start method, which starts by tokenizing the inputs and finally executes the trainer written with Python. At the end of the work, the created model is saved in the predefined path in the config.py file.

  • preprocessor.py: This file contains the preprocessing class and data preparation for use in the educational model. Unuseful patterns in the data text are deleted by the class.  



## Data Directory   
Data directory was deleted from this repository. if your task has data for fine-tuning and pre-trained data. you can create a data directory like this:

    FINE_TUNING_CORPUS_PATH: str = "data/corpus/fine_tuning/"
    PRE_TRAINING_CORPUS_PATH: str = "data/corpus/pre_training/"
    
    FINE_TUNING_FILENAME:str = "fine_tuning_corpus.txt"
    PRE_TRAINING_FILENAME:str = "pre_training_corpus.txt"
  ## Contact us  
   email pooyachavoshi@gmail.com.com .  

## Acknowledgements  
- [Readme.so](https://github.com/octokatherine/readme.so)
- [Awesome README](https://github.com/matiassingers/awesome-readme)
- [How to write a Good readme](https://bulldogjob.com/news/449-how-to-write-a-good-readme-for-your-github-project)  

## Support  
For support, email fake@fake.com or join our Slack channel.  
