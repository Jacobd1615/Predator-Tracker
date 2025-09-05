from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError
from jose.exceptions import ExpiredSignatureError
from functools import wraps
from flask import request, jsonify

SECRET_KEY = "your_secret_key"

def encode_token(user_id, role="user"):
    payload = {
        "exp": datetime.now(timezone.utc) + timedelta(hours=1),
        "iat": datetime.now(timezone.utc),
        "sub": str(user_id),
        "role": role,
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

