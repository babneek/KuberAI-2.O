from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime
import os

# Ensure data folder exists only if not present
data_folder = os.path.join(os.path.dirname(__file__), "data")
if not os.path.exists(data_folder):
    os.makedirs(data_folder)

# SQLite database file in backend/data folder
DATABASE_URL = f"sqlite:///{os.path.join(data_folder, 'gold_investments.db')}"

engine = create_engine(DATABASE_URL, echo=False)
Base = declarative_base()

class Investment(Base):
    __tablename__ = "investments"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    gold_price = Column(Float, nullable=False)
    weight = Column(Float, nullable=False)
    invested_at = Column(DateTime, default=datetime.utcnow)

Base.metadata.create_all(engine)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

def save_investment(username, amount, gold_price, weight):
    session = SessionLocal()
    try:
        print("Saving investment for:", username, amount, gold_price, weight)
        investment = Investment(
            username=username,
            amount=amount,
            gold_price=gold_price,
            weight=weight,
            invested_at=datetime.utcnow()
        )
        session.add(investment)
        session.commit()
        return True
    except Exception as e:
        print("DB Error:", e)
        session.rollback()
        return False
    finally:
        session.close()