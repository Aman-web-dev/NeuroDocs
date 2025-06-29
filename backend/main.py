from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def read_root():
    return {"message":"Hello Fast API is Running"}



@app.post("/")
def upload_doc():
    return {"Message":"Here You can Upload any document you want"}