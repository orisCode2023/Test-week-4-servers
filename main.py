from fastapi import FastAPI, HTTPException

app = FastAPI()

def write_to_file(data):
    with open("names.txt", 'a') as f:
        f.write(f"\n {data}")

def write_to_json():
    pass

@app.get("/test")
def greet():
    return {"msg": "Hi from test"}


@app.get("/test/{name}")
def get_test_name(name: str):
    write_to_file(name)
    return {"msg": "saved user"}

# @app.post("/caesar")
# def get_decrypt_ot_encrypt():
#     return { "text": string, "offset": int, "mode": "encrypt"/”decrypt”  }

@app.get("/caesar/encrypt")
def encrypt_ceaser(text: str):
    text = text.lower()
    encrypt = ""
    for char in text:
        if char == 'z':
            encrypt += 'b'
        elif char == 'y':
            encrypt += 'a'
        else:
            print(chr(ord(char) + 2))
            encrypt += chr(ord(char) + 2)

    return {"encrypted_text": encrypt}

@app.post("/caesar/decrypt")
def decrypt(text: str):
    decrypt_txt = ""
    for char in text:
        if char == 'b':
            decrypt_txt += 'z'
        elif char == 'a':
            decrypt_txt += 'y'
        else:
            decrypt_txt += chr(ord(char) - 2)
    return {"decrypted_text": decrypt_txt }