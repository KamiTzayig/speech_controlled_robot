from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    # Your GPIO control code here
    return {"message": "GPIO controlled"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8888)
