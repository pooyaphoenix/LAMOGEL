from sqlmodel import create_engine, SQLModel
from db.chat_session import ChatSession
from urllib.parse import quote

user = 'pooya'
password = 'kFBfBmBXRMBA'
address = '172.21.30.21'
port = '30799'
db_name ='dev_data'

engine = create_engine(url=f"mysql://{user}:{password}@{address}:{port}/{db_name}".
                        format(user=user, 
                               password=password, 
                               address=address,
                               port=port,
                               db_name=db_name), 
                        echo=False
                        )

# SQLModel.metadata.create_all(engine)