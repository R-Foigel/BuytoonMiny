from sqlalchemy import Column, Integer, DECIMAL, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

# הגדרת Base
Base = declarative_base()

class ConcreteRequest(Base):
    __tablename__ = 'ConcreteRequests'

    request_id = Column(Integer, primary_key=True, autoincrement=True)  # מזהה ייחודי
    customer_id = Column(Integer, ForeignKey('Customers.id'))  # קישור ללקוח
    purpose_id = Column(Integer)  # סוג הבקשה
    quantity = Column(DECIMAL(6, 2))  # כמות
    address = Column(String(255))  # כתובת
    lat = Column(DECIMAL(9, 6), nullable=False)  # רוחב
    lng = Column(DECIMAL(9, 6), nullable=False)  # אורך

    # קשרים
    customer = relationship("Customer", back_populates="concrete_requests")
    contractor_requests = relationship("ContractorConcreteRequest", back_populates="concrete_request")