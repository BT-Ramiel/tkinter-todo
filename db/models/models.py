from datetime import datetime
from typing import List, Optional
from uuid import UUID

from sqlalchemy import CheckConstraint, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.models.BaseClass import Base
from db.Utils.generateDataTypes import generate_uuid


class Task(Base):
    __tablename__ = "task"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=generate_uuid)
    title: Mapped[str] = mapped_column(String(100))
    description: Mapped[Optional[str]] = mapped_column(String(1000))
    status: Mapped[str] = mapped_column(
        CheckConstraint("status IN ('pending','in_progress','completed')"),
        default="pending",
    )
    priority: Mapped[str] = mapped_column(
        CheckConstraint("priority IN ('normal','medium','high')"), default="normal"
    )
    due_date: Mapped[Optional[datetime]]

    task_comments: Mapped[List["TaskComment"]] = relationship(
        "TaskComment", cascade="all,delete"
    )

    def __repr__(self) -> str:
        return f"Task(id={self.id!r}, title={self.title!r}, description={self.description!r}, status={self.status!r}, priority={self.priority!r}, due_date={self.due_date!r})"


class TaskComment(Base):
    __tablename__ = "task_comment"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=generate_uuid)
    comment: Mapped[str] = mapped_column(String(200))

    task_id: Mapped[UUID] = mapped_column(ForeignKey("task.id", ondelete="CASCADE"))
    task: Mapped["Task"] = relationship(foreign_keys=[task_id])

    def __repr__(self) -> str:
        return f"comment={self.comment!r}, task_id={self.task_id!r})"
