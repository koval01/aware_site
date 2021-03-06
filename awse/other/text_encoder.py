from base64 import b64encode as encoder
from random import choice
from string import ascii_letters, digits


def generate_(length=24) -> str:
    return "".join([choice(ascii_letters + digits) for _ in range(length)])


def encode(text: str) -> str:
    pos_ = 3 + 1
    str_ = choice(ascii_letters)
    rnd_ = generate_()
    enc_ = encoder(bytes(str(text), 'utf-8')).decode("utf-8")

    return str_ + enc_[:pos_] + rnd_ + enc_[pos_:]
