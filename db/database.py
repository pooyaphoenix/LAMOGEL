from sqlmodel import create_engine, SQLModel, Session
import db.model_list
from config import Config
from core.tools import tls
from core.singletone_class import SingletonClass


class Database(metaclass=SingletonClass):
    def __init__(self) -> None:
        self.user = Config.DB['USER']
        self.password = Config.DB['PASSWORD']
        self.address = Config.DB['ADDRESS']
        self.port = Config.DB['PORT']
        self.db_name = Config.DB['DB_NAME']

        tls.log("engine created.")

        self.engine = create_engine(url=f"mysql://{self.user}:{self.password}@{self.address}:{self.port}/{self.db_name}".
                                    format(user=self.user,
                                           password=self.password,
                                           address=self.address,
                                           port=self.port,
                                           db_name=self.db_name),
                                    echo=Config.DEBUG_MODE
                                    )

    def get_session(self) -> Session:
        with Session(self.engine) as session:
            return session

    def migrate_db(self):
        SQLModel.metadata.create_all(self.engine)
