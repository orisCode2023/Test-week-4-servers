from fastapi import FastAPI, HTTPException

app = FastAPI()

def write_to_file(data):
    with open("names.txt", 'a') as f:
        f.write(f"\n {data}")

def create_alphabetic_list():
    lst = []
    for char in range(ord('a'), ord('z') + 1):
        lst.append(chr(char))
    return lst


@app.get("/test")
def greet():
    return {"msg": "Hi from test"}


@app.get("/test/{name}")
def get_test_name(name: str):
    write_to_file(name)
    return {"msg": "saved user"}

@app.post("/caesar")
def get_decrypt_ot_encrypt(body: dict):
    return { "text": body["text"], "offset": body["offset"], "mode": body["mode"]}

@app.get("/caesar/encrypt")
def encrypt_ceaser(text: str, offset: int):
    alphabetic = create_alphabetic_list()
    text = text.lower()
    encrypt = ""
    for char in text:
        value = alphabetic.index(char)
        char = alphabetic[(value + offset) % len(alphabetic)]
        encrypt += char
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

@app.get("/fence/encrypt")
def encrypt_fence(txt: str):
    pair = odd = ""
    for char in range(len(txt)):
        if char % 2 == 0:
            pair += txt[char]
        else:
            odd += txt[char]
    return pair + odd


@app.post("/fence/decrypt")
def decrypt_fence(txt: str):
    pair = txt[:len(txt) // 2]
    odd = txt[len(txt) // 2:]
    decrypt = ""
    for i in range(len(txt) // 2):
        decrypt += pair[i]
        decrypt += odd[i]
    return decrypt
