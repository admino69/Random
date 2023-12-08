import bcrypt

password = "test123"
salt = bcrypt.gensalt(rounds=10)
hashed_password = bcrypt.passpw(password, salt)
print("hashed_password)
