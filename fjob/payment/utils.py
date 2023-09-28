import hashlib
import secrets


def generate_random_id() -> str:
    random_data = secrets.token_bytes(500)
    sha512_hash = hashlib.sha512()
    sha512_hash.update(random_data)
    hash_value = sha512_hash.hexdigest()
    return hash_value
