import os
import base64
import hashlib
from cryptography.hazmat.primitives.ciphers.aead import AESGCM


def derive_key(password: str, salt: bytes) -> bytes:
    return hashlib.pbkdf2_hmac(
        "sha256",
        password.encode(),
        salt,
        600_000,
        dklen=32
    )


def encrypt(text: str, password: str) -> str:
    salt = os.urandom(16)
    nonce = os.urandom(12)

    key = derive_key(password, salt)
    encrypted = AESGCM(key).encrypt(
        nonce,
        text.encode(),
        None
    )

    data = salt + nonce + encrypted
    return base64.b64encode(data).decode()


def decrypt(data: str, password: str) -> str:
    raw = base64.b64decode(data)

    salt = raw[:16]
    nonce = raw[16:28]
    encrypted = raw[28:]

    key = derive_key(password, salt)

    decrypted = AESGCM(key).decrypt(
        nonce,
        encrypted,
        None
    )

    return decrypted.decode()
