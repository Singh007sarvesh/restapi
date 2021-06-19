from pydantic import BaseModel, ValidationError, validator

class SchemaCustomerInfo(BaseModel):
	firstName: str
	lastName: str
	emailID: str
	mobileNumber: int
	password: str