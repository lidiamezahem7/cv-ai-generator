from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from ai_service import rewrite_cv

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "API CV IA opérationnelle"}

@app.post("/optimize")
async def optimize_cv(file: UploadFile = File(...)):
    text = (await file.read()).decode("utf-8", errors="ignore")
    optimized = rewrite_cv(text)
    return {"optimized": optimized}
