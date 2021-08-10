from cryptography.fernet import Fernet
import os

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("key.key", "rb").read()

def encrypt_string(string, key):
    f = Fernet(key)
    return f.encrypt(string.encode())

def decrypt_string(string, key):
     f = Fernet(key)
     return f.decrypt(string).decode()

def encrypt_file(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        file_data = file.read()
        encrypted_data = f.encrypt(file_data)
    with open(filename, "wb") as file:
        file.write(encrypted_data)

def encrypt_file_name(filename,key):
    os.rename(filename,os.path.join(os.path.dirname(filename),encrypt_string(filename,key).decode()))

def decrypt_file_name(filename,key):
    if(os.path.isfile(filename)):
        os.rename(
            filename,
            decrypt_string(os.path.basename(filename.encode()),key)
        )
   
def decrypt_file(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(filename, "wb") as file:
        file.write(decrypted_data)

def encrypt_folder(directory, key):
    for root, dirs, files in os.walk(directory):
        [encrypt_file(os.path.join(root,name),key) for name in files]

def decrypt_folder(directory, key):
    for root, dirs, files in os.walk(directory):
        [decrypt_file(os.path.join(root,name),key) for name in files]

def encrypt_filenames_in_folder(directory, key):
    for root, dirs, files in os.walk(directory):
        [encrypt_file_name(os.path.join(root,name),key) for name in files]

def decrypt_filenames_in_folder(directory, key):
    for root, dirs, files in os.walk(directory):
        [decrypt_file_name(os.path.join(root,name),key) for name in files]

def encrypt_files_and_filenames_in_folder(directory, key):
    encrypt_folder(directory,key)
    encrypt_filenames_in_folder(directory,key)

def decrypt_files_and_filenames_in_folder(directory, key):
    decrypt_folder(directory, key)
    decrypt_filenames_in_folder(directory, key)
