from datetime import datetime
from typing import List

from sqlalchemy import CheckConstraint, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.models.BaseClass import Base
from db.Utils.generateDataTypes import generate_uuid


class User(Base):
    __tablename__ = "user"

    id: Mapped[str] = mapped_column(primary_key=True, default=generate_uuid)
    username: Mapped[str] = mapped_column(String(30))
    password: Mapped[str] = mapped_column(String(100))

    tasks: Mapped[List["Task"]] = relationship(
        back_populates="user", cascade="all,delete"
    )

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, username={self.username!r}, password={self.password!r})"


class Task(Base):
    __tablename__ = "task"

    id: Mapped[str] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100))
    description: Mapped[str] = mapped_column(String(1000))
    status: Mapped[str] = mapped_column(
        CheckConstraint("status IN ('pending','in_progress','completed')")
    )
    priority: Mapped[str] = mapped_column(
        CheckConstraint("priority IN ('normal','medium','high')")
    )
    due_date: Mapped[datetime]

    user_id: Mapped[str] = mapped_column(ForeignKey("user.id", ondelete="CASCADE"))
    user: Mapped["User"] = relationship(foreign_keys=[user_id])

    task_comments: Mapped[List["TaskComment"]] = relationship(
        back_populates="task", cascade="all,delete"
    )

    def __repr__(self) -> str:
        return f"Task(id={self.id!r}, title={self.title!r}, description={self.description!r}, status={self.status!r}, priority={self.priority!r}, due_date={self.due_date!r}, user id={self.user_id!r})"


class TaskComment(Base):
    __tablename__ = "task_comment"

    id: Mapped[str] = mapped_column(primary_key=True)
    comment: Mapped[str] = mapped_column(String(200))

    task_id: Mapped[str] = mapped_column(ForeignKey("task.id", ondelete="CASCADE"))
    task: Mapped["Task"] = relationship(foreign_keys=[task_id])

    def __repr__(self) -> str:
        return (
            f"User(id={self.id!r}, comment={self.comment!r}, task_id={self.task_id!r})"
        )