from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from ai_service import generate_cv

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "API CV IA opérationnelle avec OpenAI"}

@app.post("/generate")
async def generate(file: UploadFile = File(...)):
    text = (await file.read()).decode("utf-8", errors="ignore")
    result = await generate_cv(text)
    return {"cv": result}