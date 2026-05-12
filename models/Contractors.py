from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Contractor(Base):
    __tablename__ = 'Contractors'

    id = Column(Integer, primary_key=True, autoincrement=True)  # מזהה קבלן
    name = Column(String(15))  # שם הקבלן
    phone = Column(String(15))  # טלפון

    # קשר לטבלת ContractorConcreteRequests
    contractor_requests = relationship("ContractorConcreteRequest", back_populates="contractor")