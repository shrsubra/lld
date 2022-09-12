from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Float, Integer, ForeignKey, String

Base = declarative_base()


class Location(Base):
    __tablename__ = "atm_location"
    location_id = Column(Integer, primary_key=True, autoincrement=True)
    city = Column(String, nullable=False)
    state = Column(String, nullable=False)
    country = Column(String, nullable=False)
    zip = Column(String, nullable=False)
    adddress = Column(String, nullable=False)
    coordinates = Column(String, nullable=True)


class Atm(Base):
    __tablename__ = "atm"
    atm_id = Column(Integer, primary_key=True, autoincrement=True)
    cash_balances = Column(Float, nullable=False)
    check_balances = Column(Float, nullable=False)
    location_id = Column(Integer, ForeignKey(Location.location_id))


from sqlalchemy import create_engine
engine = create_engine("postgresql://postgres:postgres@localhost:5432/atm", echo=True, future=True)
Base.metadata.create_all(engine)


if __name__ == "__main__":
    pass





