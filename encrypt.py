from cryptography.fernet import Fernet
import os

def generate_key():
    key = Fernet.generate_key()
    with open("key.txt" , "wb") as keyy:
        keyy.write(key)
        
    
def load_key():
    with open("key.txt" , "rb") as s_key:
        key = s_key.read()
        return key
    
def encrypt(name , key):
    m = Fernet(key)
    with open(name , "rb") as file:
        data = file.read()
        e_DATA = m.encrypt(data)
        open(name , "wb").write(e_DATA)


if not os.path.isfile("key.txt") :
    generate_key()


key = load_key()
encrypt("img.jpg", key)