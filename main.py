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
#     pass

# @app.get()
# def encrypt(text: str):
#     pass

# @app.post()
# def decrypt():
#     pass