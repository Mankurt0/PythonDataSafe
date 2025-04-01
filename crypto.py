from cryptography.fernet import Fernet
import bcrypt

def hashpass(password: str) -> bytes:
    encpassword = password.encode()
    hashedpassword = bcrypt.hashpw(encpassword, bcrypt.gensalt())
    return hashedpassword

def checkhash(password, hashedpassword) -> bool:
    encpassword = password.encode()
    if bcrypt.checkpw(encpassword, hashedpassword):
        return True
    else:
        return False

print(hashpass("Гооол"))
print(checkhash("Гооол", b'$2b$12$U3SyJjNB7XJI4V45TRmcCukA5An8BKe7oJEW6R57UbZLlgxBtk06m'))

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