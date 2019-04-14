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

def encrypt_file(file_name):
    f = Fernet(getKey())
    with open(file_name,'rb') as file:
        encrypted_file =f.encrypt(file.read())
    file.close()

    write_file_name = file_name.split(".")[0]
    write_file = open("%s.enc"%(write_file_name),"wb")
    write_file.write(encrypted_file)
    write_file.close()

def decrypt(file_name):
    try:
        file=open(file_name,"rb")
        encrypted_message=file.read()
        file.close()
        f = Fernet(getKey())
        decrypted_message=f.decrypt(encrypted_message)
        message = decrypted_message.decode()

        write_file_name = 'decrypted_'+file_name.split(".")[0]+".txt"
        write_file = open(write_file_name,"w")
        write_file.write(message)
        write_file.close()
    except :
        print("Incorrect Key")


#commandline args
args = sys.argv[1:]
if(args!=[]):
    if(args[0].lower() == 'generate_key'):
        generate_key()
    elif(args[0].lower()  == 'encrypt'):
        encrypt(args[1])
    elif(args[0].lower() == 'encrypt_file'):
        encrypt_file(args[1])
    elif(args[0].lower() == 'decrypt'):
        decrypt(args[1])
else:
    print("Please enter a command")
