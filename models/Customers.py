from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Customer(Base):
    __tablename__ = 'Customers'

    id = Column(Integer, primary_key=True, autoincrement=True)  # מזהה ייחודי
    name = Column(String(15))  # שם הלקוח
    phone = Column(String(20))  # טלפון

    # קשר לבקשות בטון
    concrete_requests = relationship("ConcreteRequest", back_populates="customer")