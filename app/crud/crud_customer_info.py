from app.db.session import db
from app.models.model_customer_info import CustomerINFO
from sqlalchemy import and_
# Import writer class from csv module


def create(obj):
	try:
		db.add(obj)
		db.commit()
		db.refresh(obj)
		db.close()
		return 1
	except Exception as e:
		db.close()
		return e

def update(customerID, obj_in):
	flag = 0
	for itr in db.query(CustomerINFO).filter(and_(
		CustomerINFO.customerID == customerID)).all():
		flag = 1
		if obj_in.firstName != "":
			itr.firstName = obj_in.firstName
		if obj_in.lastName != "":
			itr.lastName = obj_in.lastName
		if obj_in.emailID != "":
			itr.emailID = obj_in.emailID
		if obj_in.mobileNumber != "":
			itr.mobileNumber = obj_in.mobileNumber
		if obj_in.password != "":
			itr.password = obj_in.password
	if flag == 0:
		return 0
	db.commit()
	db.close()
	return 1

def get():
	rows = db.query(CustomerINFO).all()
	db.close()
	return rows

def delete(customerID):
	try:
		obj = db.query(CustomerINFO).filter_by(customerID=customerID).one()
		db.delete(obj)
		db.commit()
		db.close()
		return 1
	except:
		db.close()
		return 0