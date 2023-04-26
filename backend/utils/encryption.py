import bcrypt


def encrypt(password: str):
    return bcrypt.hashpw(password.encode(), 10)


def decrypt(password: str, hashed_password: str):
    return bcrypt.checkpw(password.encode(), hashed_password.encode())
