from sqlmodel import Session,select
from urllib.parse import urljoin
from db.db import engine
from db.chat_session import ChatSession
import json
from kernel.color import color


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
        print(color.BOLD + color.BLUE + "Fetching chat sessions from DB..." + color.END)
        message_list: list = []
        with Session(engine) as session:
            chats = session.exec(select(ChatSession)).all()
        for chat in chats:
            message_list.append([(c[1]) for c in chat if c[0] == 'message'])
            
        return message_list

    
    def set_offset(self, sum:int = 0):
        
        f = open(self.offset_file_path)
        before_sum = json.load(f)
        with open(self.offset_file_path, 'w', encoding='utf-8') as f:
            data = before_sum['count'] + sum
            json.dump({'count': int(data)}, f, ensure_ascii=False, indent=4)
        print('done')
    


   