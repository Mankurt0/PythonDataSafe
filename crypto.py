from cryptography.fernet import Fernet
import bcrypt

key = Fernet.generate_key() 
f = Fernet(key)
message = "Сообщение".encode()
enc = f.encrypt(message)
print(enc)
print(f.decrypt(enc).decode())

password = b"password" #Ввод пароля
hashed = bcrypt.hashpw(password, bcrypt.gensalt()) #Хэшированый пароль
if bcrypt.checkpw(password, hashed): #Проверка пароля
     print("подходит")
else:
     print("не подходит")