from sqlite3 import ProgrammingError

from sqlalchemy import create_engine, engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

from db.models.models import Task, TaskComment


class Controller:
    def __init__(self) -> None:
        controller_engine = create_engine("sqlite:///db/database.db", echo=True)
        session = sessionmaker(bind=controller_engine)
        self.session = session()

    def create_empty_task(self, task_title):
        task = self.session.query(Task).filter(Task.title == task_title).first()
        if task == None:
            new_task = Task()
            new_task.title = task_title
            self.session.add(new_task)
            self.session.commit()
        else:
            raise ProgrammingError("This task title is already in use")
