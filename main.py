from cryptography.fernet import Fernet
import sys

def generate_key():
    key = Fernet.generate_key()
    key_text = open("key.key","wb")
    key_text.write(key)
    key_text.close()
    print("Key generated succesfully")

def getKey():
    file=open("key.key","rb")
    key = file.read()
    file.close()
    return key

def encrypt(message):
    #encrypt message
    encoded = message.encode()
    f= Fernet(getKey())
    encrypted = f.encrypt(encoded)

    #store encrptes string
    file = open("message.key","wb")
    file.write(encrypted)
    file.close()

    print("Message encrypted succesfully")

def decrypt(file_name):
    try:
        file=open(file_name,"rb")
        encrypted_message=file.read()
        file.close()
        f = Fernet(getKey())
        decrypted_message=f.decrypt(encrypted_message)
        message = decrypted_message.decode()
        print(message)
    except:
        print("Incorrect Key")


#commandline args
args = sys.argv[1:]
if(args!=[]):
    if(args[0].lower() == 'generate_key'):
        generate_key()
    elif(args[0].lower()  == 'encrypt'):
        encrypt(args[1])
    elif(args[0].lower() == 'decrypt'):
        decrypt(args[1])
else:
    print("Please enter a command")
