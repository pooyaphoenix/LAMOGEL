from typing import Optional
from sqlmodel import Field, SQLModel
from datetime import datetime
from sqlalchemy import UniqueConstraint


class ChatSessionModel(SQLModel, table=True):
    __tablename__ = "chatsession"
    id: Optional[int] = Field(default=None, primary_key=True)
    session_id: str = Field(index=True)
    fingerprint: str = Field(default=None)
    message: str = Field(default=None)
    intent: str = Field(default=None)
    created_at: datetime = Field(
        default_factory=datetime.utcnow, nullable=False)
    updated_at: datetime = Field(
        default_factory=datetime.utcnow, nullable=False)
