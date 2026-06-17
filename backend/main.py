from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from ai_service import generate_cv
import openai
import logging
import os 

print("OPENAI_API_KEY =", os.getenv("OPENAI_API_KEY"))

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

logging.basicConfig(level=logging.INFO)

@app.get("/")
def home():
    return {"message": "API CV IA opérationnelle avec OpenAI"}

@app.post("/generate")
async def generate(file: UploadFile = File(...)):
    text = (await file.read()).decode("utf-8", errors="ignore")
    try:
        result = await generate_cv(text)
        return {"cv": result}
    except openai.error.OpenAIError as oe:
        logging.error(f"OpenAI API error: {oe}")
        raise HTTPException(status_code=500, detail=f"OpenAI API error: {oe}")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        raise HTTPException(status_code=500, detail=f"Unexpected error: {e}")