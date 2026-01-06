from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from ai_engine import ai_engine
import uvicorn

app = FastAPI()

# Configure CORS to allow requests from your React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Allow all origins for dev
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class AnalyzeRequest(BaseModel):
    image: str  # Base64 string
    targetLanguage: str | None = None

@app.post("/analyze")
async def analyze_page(request: AnalyzeRequest):
    try:
        # Call the AI engine
        html_content = ai_engine.generate_html(request.image, request.targetLanguage)
        return {"html": html_content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
