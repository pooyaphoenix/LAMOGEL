from sqlmodel import Session,select
from urllib.parse import urljoin
from db.db import engine
from db.chat_session import ChatSession
import json

class ChatSessionHandler:

    offset_file_path:str = "db/offset_file_path.json"

    def __init__(self) -> None:
        self.model = ChatSession()

    def get_one(self, fingerprint:str = ""):
        with Session(engine) as session:
            statement = select(ChatSession).where(ChatSession.fingerprint == fingerprint)
            results = session.exec(statement)
            for session in results:
                return results
        return False
    
    def get_all(self):
        print("Fetching chat sessions from DB...")
        with Session(engine) as session:
            chats = session.exec(select(ChatSession)).all()
        return chats

    
    def set_offset(self, sum:int = 0):
        
        f = open(self.offset_file_path)
        before_sum = json.load(f)
        with open(self.offset_file_path, 'w', encoding='utf-8') as f:
            data = before_sum['count'] + sum
            json.dump({'count': int(data)}, f, ensure_ascii=False, indent=4)
        print('done')
    


   