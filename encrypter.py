import os
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def initialize_bin(filename):
    inital=open(filename,"rb")
    bin=open("encrypted.bin","wb")
    bin.write(inital.read())
    bin.close()
    return f'{os.getcwd()}\\encrypted.bin'
def deleteFile():
    os.remove("encrypted.bin")

def encrypt():
    file=open("encrypted.bin","rb")
    key=get_random_bytes(32)
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(file.read())
    key_out=open("filekey.key","wb")
    key_out.write(key)
    key_out.close()
    file_out = open("encrypted.bin", "wb")
    [ file_out.write(x) for x in (cipher.nonce, tag, ciphertext) ]
    file_out.close()
    print("i ran encrypt")


def decrypt():
    file_in = open("encrypted.bin", "rb")
    nonce, tag, ciphertext = [ file_in.read(x) for x in (16, 16, -1) ]
    file_in.close()
    key_in=open("filekey.key","rb")
    key=key_in.read()
    cipher = AES.new(key, AES.MODE_EAX, nonce)
    data = cipher.decrypt_and_verify(ciphertext, tag)
    file_out=open("encrypted.bin", "wb")
    file_out.write(data)
    file_out.close()
    print("i ran decrypt")

