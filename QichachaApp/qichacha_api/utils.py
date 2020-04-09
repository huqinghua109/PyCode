import hashlib
import time

def get_current_timestamp():
    return int(time.time())

def create_signature(api_key, secret_key, timestamp_str):
    if api_key == "" or secret_key == "":
        print("secret_key or api_key is none")
        return
    md5 = hashlib.md5()
    query_string = api_key + timestamp_str + secret_key
    md5.update(query_string.encode(encoding='utf-8'))
    signature = md5.hexdigest().upper()
    print(signature)
    return signature
