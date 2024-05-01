from sqlalchemy import create_engine

from db.models.models import Base

if __name__ == "__main__":
    engine = create_engine("sqlite:///db/database.db", echo=True)
    Base.metadata.create_all(engine)
