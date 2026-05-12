from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Customer, Contractor, ConcreteRequest, ContractorConcreteRequest
from .Base import Base, session
from .Customers import Customer
from .Contractors import Contractor
from .ConcreteRequests import ConcreteRequest
from .ContractorConcreteRequests import ContractorConcreteRequest
# הגדרת חיבור למסד
DATABASE_URL = "mssql+pyodbc://username:password@localhost/beton?driver=ODBC+Driver+17+for+SQL+Server"
engine = create_engine(DATABASE_URL, echo=True)
Session = sessionmaker(bind=engine)
session = Session()

# יצירת טבלאות אם לא קיימות
Base.metadata.create_all(engine)

# דוגמה: הוספת לקוח
new_customer = Customer(name="David", phone="0501234567")
session.add(new_customer)
session.commit()

# קריאה מהטבלה
customers = session.query(Customer).all()
for c in customers:
    print(c.id, c.name, c.phone)