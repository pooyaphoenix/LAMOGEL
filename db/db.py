from sqlmodel import create_engine, SQLModel
from db.chat_session import ChatSession
from urllib.parse import quote
from config import Config

user = Config.db['USER']
password = Config.db['PASSWORD']
address = Config.db['ADDRESS']
port = Config.db['PORT']
db_name = Config.db['DB_NAME']

engine = create_engine(url=f"mysql://{user}:{password}@{address}:{port}/{db_name}".
                        format(user=user, 
                               password=password, 
                               address=address,
                               port=port,
                               db_name=db_name), 
                        echo=False
                        )

# SQLModel.metadata.create_all(engine)