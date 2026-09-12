"""Password generator. Used AI in the initial"""

import secrets
import string

def generate(length=12, use_symbols=True):
    chars = string.ascii_letters + string.digits
    if use_symbols:
        chars += string.punctuation
    return ''.join(secrets.choice(chars) for _ in range(length))

if __name__ == "__main__":
    print(generate())   