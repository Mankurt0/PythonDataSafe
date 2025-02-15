from cryptography.fernet import Fernet
import bcrypt
from interface import entlogin, entpassword

def hashpass(password: str) -> bytes:
    encpassword = password.encode()
    hashedpassword = bcrypt.hashpw(encpassword, bcrypt.gensalt())
    return hashedpassword

print(hashpass(entpassword))

""" key = Fernet.generate_key() 
f = Fernet(key)
message = "Сообщение".encode()
enc = f.encrypt(message)
print(enc)
print(f.decrypt(enc).decode())

#password = b"password" #Ввод пароля
password = "password"
password = password.encode()
hashed = bcrypt.hashpw(password, bcrypt.gensalt()) #Хэшированый пароль
if bcrypt.checkpw(password, hashed): #Проверка пароля
     print("подходит")
else:
     print("не подходит") """