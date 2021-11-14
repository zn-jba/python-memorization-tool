from sqlalchemy import create_engine
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB_NAME = "flashcard.db"
Base = declarative_base()


class Flashcard(Base):
    __tablename__ = "flashcard"

    id = Column(Integer, primary_key=True)
    question = Column(String(255))
    answer = Column(String(255))
    box = Column(Integer, default=1)

    def __str__(self) -> str:
        return f"{self.question}\n{self.answer}"

    @staticmethod
    def find_all() -> list["Flashcard"]:
        return session.query(Flashcard).all()

    @staticmethod
    def find_by_id(_id: int) -> "Flashcard":
        return session.query(Flashcard).get(_id)

    @staticmethod
    def update_card(card: "Flashcard",
                    question: str = None,
                    answer: str = None,
                    box: int = None) -> None:
        new_values = {}
        if question:
            new_values["question"] = question
        if answer:
            new_values["answer"] = answer
        if box:
            new_values["box"] = box
        if new_values:
            session.query(Flashcard).filter(Flashcard.id == card.id).update(new_values)
            session.commit()

    @staticmethod
    def delete_card(card: "Flashcard") -> None:
        query = session.query(Flashcard).filter(Flashcard.id == card.id)
        if query:
            query.delete()
            session.commit()

    @staticmethod
    def add_flashcard(question: str, answer: str) -> "Flashcard":
        flashcard = Flashcard(question=question, answer=answer)
        session.add(flashcard)
        session.commit()
        return flashcard


engine = create_engine(f"sqlite:///{DB_NAME}?check_same_thread=False")
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
