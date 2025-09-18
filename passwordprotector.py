
import hashlib

def hash_password(password):
    encrypted_password = hashlib.sha256(password.encode())
    encrypted_password = encrypted_password.hexdigest()
    return encrypted_password

password = input("Skriv inn et passord: ")

encrypted_password = hash_password(password)

print("Originalt passord:", password)
print("Hashet passord:", encrypted_password)