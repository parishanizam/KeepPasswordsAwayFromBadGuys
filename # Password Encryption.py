# Password Encryption

#python has a base64 library we can use to manipulate the inputed password
import base64
# user can imput their password that will be taken in as a string
password=input("Please input your password to be encrypted: ")
# calling encode("utf-8") will change the string into a UTF-8 string
encrypted_password = password.encode("utf-8")
#Calling base.64.b64encode which is a built in function in the base64 library, 
#will encode the string into base 64 string
encoded = base64.b64encode(encrypted_password)
#prunt the encrypted password
print(encoded)
