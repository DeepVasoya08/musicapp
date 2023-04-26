import os
from typing import Annotated

import jwt
from dotenv import load_dotenv
from fastapi import Header

load_dotenv()

jwt_secret = os.getenv("jwt_secret")
algoritham = os.getenv("algoritham")


def generateToken(payload):
    return jwt.encode(payload, jwt_secret, algorithm=algoritham)


async def verifyToken(token: Annotated[str, Header()]):
    return jwt.decode(token, jwt_secret, algorithms=algoritham)
