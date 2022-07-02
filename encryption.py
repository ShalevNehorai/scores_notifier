import os
import base64
from cryptography.fernet import Fernet
from dotenv import load_dotenv

load_dotenv()

"""
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
"""

def load_key():
    return open("key.key", "rb").read()

key = load_key() #Fernet.generate_key()
fernet = Fernet(key)

def encrypt(message):
    print(key)
    return fernet.encrypt(message.encode())

def decrypt(enc_message):
    return fernet.decrypt(enc_message).decode()
