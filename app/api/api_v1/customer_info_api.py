from fastapi import APIRouter, Depends, HTTPException, Response, status, Form
from fastapi import File, UploadFile
import os
from app.core.applogger import applogger
from app.core.validation import (is_mobile_number_valid, email_id_validation) 
from typing import Optional
from fastapi.encoders import jsonable_encoder
from starlette.status import (HTTP_201_CREATED, HTTP_200_OK, HTTP_400_BAD_REQUEST,
	HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR)
from app.schemas.schema_customer_info import SchemaCustomerInfo
from app.models.model_customer_info import CustomerINFO
from app.crud.crud_customer_info import create, update, get, delete
import json
router = APIRouter()

@router.post("/customers")
def create_customer_info(response:Response, requestInput: SchemaCustomerInfo):
	try:
		if not is_mobile_number_valid(requestInput.mobileNumber):
			applogger.error('Bad Request, Please provide mobile number in the following format %s'%(
					'The first digit should contain number between 7 to 9.'))
			response.status_code = status.HTTP_400_BAD_REQUEST
			return {"response":'Bad Request, Please provide mobile number in the following format %s'%(
					'The first digit should contain number between 7 to 9.')}
		if not email_id_validation(requestInput.emailID):
			applogger.error('Bad Request, Please provide email id in proper format.')
			response.status_code = status.HTTP_400_BAD_REQUEST
			return {"response":'Bad Request, Please provide email id in proper format.'}
		customerINFO = CustomerINFO()
		customerINFO.firstName = requestInput.firstName
		customerINFO.lastName = requestInput.lastName
		customerINFO.emailID = requestInput.emailID
		customerINFO.mobileNumber = requestInput.mobileNumber
		customerINFO.password = requestInput.password
		db_response = create(customerINFO)
		if db_response == 1:
			response.status_code=status.HTTP_201_CREATED
			applogger.info("Successfully added to customer table")
			return {'response': "Successfully Added."}
		else:
			response.status_code=status.HTTP_400_BAD_REQUEST
			applogger.error(str(db_response))
			return {"response":str(db_response)}
	except Exception as e:
		response.status_code=status.HTTP_400_BAD_REQUEST
		applogger.error(str(e))
		return {"response":str(e)}


@router.put("/customers/{customerID}")
def update_customer_info(response:Response, requestInput: SchemaCustomerInfo,customerID):
	try:
		db_response = update(customerID, requestInput)
		if db_response == 0:
			response.status_code=status.HTTP_404_NOT_FOUND
			applogger.info("Data not found in customerINFO table")
			return {"response":"Data not found in database"}
		else:
			response.status_code = status.HTTP_200_OK
			applogger.info("Updated customerINFO table based on customerID")
			return {"response":"Updated Successfully."}
	except:
		response.status_code=status.HTTP_400_BAD_REQUEST
		applogger.error(str(e))
		return {"response":str(e)}

@router.get("/customers/{customerID}")
def get_customer_info(response:Response, customerID):
	try:
		rows = get(customerID)
		batch_data = []
		for row in rows:
			batch_data.append({
				'customerID':row.customerID,
				'firstName':row.firstName,
				'lastName':row.lastName,
				'emailID':row.emailID,
				'mobileNumber':row.mobileNumber
				})
		applogger.info("Fatched all data from customer info table")
		response.status_code = status.HTTP_200_OK
		return {"response":batch_data}
	except Exception as e:
		response.status_code=status.HTTP_400_BAD_REQUEST
		applogger.error(str(e))
		return {"response":str(e)}

@router.delete("/customers/{customerID}")
def delete_customers_info(response:Response, customerID):
	try:
		db_response = delete(customerID)
		if db_response == 0:
			response.status_code=status.HTTP_404_NOT_FOUND
			applogger.info("Data not found in customerINFO table")
			return {"response":"Data not found in database"}
		else:
			applogger.info("Deleted data from customer info table based on customerID")
			response.status_code = status.HTTP_200_OK
			return {"response":"Deleted Successfully."}
	except Exception as e:
		response.status_code=status.HTTP_400_BAD_REQUEST
		applogger.error(str(e))
		return {"response":str(e)}
