from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    # Your GPIO control code here
    return {"message": "GPIO controlled"}

@app.get("/wakeup/start")
async def wakeup_start():
    # Your GPIO control code here
    return {"message": "Wakeup started"}

@app.get("/wakeup/stop")
async def wakeup_stop():
    # Your GPIO control code here
    return {"message": "Wakeup stopped"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8888)
