from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from automation.pipeline import run_pipeline
from dotenv import load_dotenv
import os

app = FastAPI()
security = HTTPBearer()

load_dotenv()
API_TOKEN = os.getenv("API_TOKEN")

def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    if credentials.credentials != API_TOKEN:
        raise HTTPException(status_code=403, detail="Invalid or Missing Token")
    return True

@app.post("/run")
def run_pipeline_api(payload: dict, authorized: bool = Depends(verify_token)):
    result = run_pipeline(payload)  # payload langsung dict dari JSON
    return result