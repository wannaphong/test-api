from fastapi import FastAPI, File, UploadFile
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/text/{text}")
def read_word(text: str):
    return {"word": text}

if __name__ == '__main__':
   import uvicorn
   uvicorn.run(app, host="0.0.0.0", port=5000, debug=True) 
