
user = input("Enter your ID: ")
pwd = input("Enter your Password: ")

def check_account(user, pwd):
	if user == "ja5per" and pwd == "4githu6":
		print ("ACCESS ALLOWED!!")
	else:
		print ("ACCESS REFUSED!!")


check_account(user, pwd)
