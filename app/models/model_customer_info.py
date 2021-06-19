from sqlalchemy import Column, Integer, BigInteger, VARCHAR, Text
from app.db.session import Base


class CustomerINFO(Base):

    ## table name to map the variables to column
    __tablename__ = "tbl_customer_info"

    customerID = Column('customerID', Integer, nullable=False, primary_key=True)
    firstName = Column('firstName', VARCHAR(length=200), nullable=False)
    lastName = Column('lastName', VARCHAR(length=200), nullable=True)
    mobileNumber = Column('mobileNumber', BigInteger, nullable=False)
    emailID = Column('emailID', VARCHAR(length=200), nullable=False)
    password = Column('password', VARCHAR(length=100), nullable=False)