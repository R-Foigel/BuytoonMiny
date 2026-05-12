from sqlalchemy import Column, Integer, DECIMAL, String, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

# הגדרת Base לגרסה החדשה
Base = declarative_base()

class ContractorConcreteRequest(Base):
    __tablename__ = 'ContractorConcreteRequests'

    request_id = Column(Integer, primary_key=True, autoincrement=True)  # מזהה ייחודי
    concrete_id = Column(Integer, ForeignKey('ConcreteRequests.request_id'))  # קישור לבקשה
    contractor_id = Column(Integer, ForeignKey('Contractors.id'))  # קבלן מבצע
    quantity = Column(DECIMAL(6, 2))  # כמות שהקבלן יספק
    address = Column(String(255))  # כתובת ביצוע
    lat = Column(DECIMAL(9, 6))  # רוחב
    lng = Column(DECIMAL(9, 6))  # אורך
    expiry_time = Column(DateTime)  # מועד סיום ההתחייבות

    # קשרים
    contractor = relationship("Contractor", back_populates="contractor_requests")
    concrete_request = relationship("ConcreteRequest", back_populates="contractor_requests")