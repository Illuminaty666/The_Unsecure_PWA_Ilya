import bcrypt

password = input("Password: ")
hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
print(hashed)
