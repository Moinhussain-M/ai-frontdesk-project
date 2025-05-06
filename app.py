from fastapi import FastAPI
from livekit import AccessToken, VideoGrant
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "AI Frontdesk Running"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
