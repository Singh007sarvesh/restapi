import re
import datetime


# mobile number validation
def is_mobile_number_valid(mobile_number):
	mobile_number = str(mobile_number)
	# The first digit should contain number between 7 to 9
	return re.match(r'[789]\d{9}$', mobile_number)

# email id validation
def email_id_validation(email_id):
	# Make a regular expression
	# for validating an Email
	regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
	if(re.search(regex, email_id)):
		return True
	else:
		return False