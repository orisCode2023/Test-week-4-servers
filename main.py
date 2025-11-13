from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get("/test")
def greet():
    return {"msg": "Hi from test"}


@app.get("/tests")
def get_test_name(name: str):
    return {"msg": name}

@app.post("/caesar")
def get_decrypt_ot_encrypt():
    pass

@app.get()
def encrypt(text: str):
    pass

@app.post()
def decrypt():
    pass