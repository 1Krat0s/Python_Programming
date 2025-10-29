import hmac # hash-based message authentificaiton
import hashlib

def calc_hash(key: str, message: str):
    b_key = bytes(key, "utf-8")
    b_message = bytes(message, "utf-8")

    hash_value = hmac.new(b_key, b_message, hashlib.sha256)
    return hash_value.hexdigest()


secret_key = "very_secret_key"
msg1 = calc_hash(secret_key, "Pay $100")
msg2 = calc_hash(secret_key, "Pay $100")
msg3 = calc_hash(secret_key, "Pay $1000")

print(msg1 == msg2)
print(msg2 == msg3)