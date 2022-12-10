from sqlmodel import select

from db.database import Database
from db.chat_session_model import ChatSessionModel
from core.tools import tls


class ChatSessionRepo:
    def get_one(self, fingerprint: str):
        session = Database().get_session()
        statement = select(ChatSessionModel).where(
            ChatSessionModel.fingerprint == fingerprint)
        results = session.exec(statement)
        return results


    def get_all(self):

        tls.log("Fetching chat sessions from DB...", bold=True)

        message_list: list = []
        session = Database().get_session()
        statement = select(ChatSessionModel)
        chats = session.exec(statement).all()

        for chat in chats:
            message_list.append([(c[1]) for c in chat if c[0] == 'message'])

        return message_list
