from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from generator import generate_image
from prompt_engineering import enhance_prompt


# Create FastAPI application
app = FastAPI(
    title="Stable Diffusion Text-to-Image API",
    description="Text-to-image generation using Stable Diffusion",
    version="1.0.0"
)


# Allow frontend applications to communicate with this backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Serve generated images
app.mount(
    "/generated_images",
    StaticFiles(directory="generated_images"),
    name="generated_images"
)


# Serve frontend
frontend_path = Path(__file__).resolve().parent.parent / "frontend"

app.mount(
    "/frontend",
    StaticFiles(directory=frontend_path, html=True),
    name="frontend"
)


# Request model
class GenerateRequest(BaseModel):
    prompt: str


# Home route
@app.get("/")
def home():
    return {
        "message": "Stable Diffusion Text-to-Image API is running!"
    }


# Health check
@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


# Generate image route
@app.post("/generate")
def generate(request: GenerateRequest):

    # Get the original prompt from the user
    original_prompt = request.prompt

    # Enhance the prompt using prompt engineering
    enhanced_prompt = enhance_prompt(original_prompt)

    # Generate image using the enhanced prompt
    output_path, generation_time = generate_image(
    enhanced_prompt,
    filename="generated_api_image.png"
)

    return {
    "message": "Image generated successfully!",
    "original_prompt": original_prompt,
    "enhanced_prompt": enhanced_prompt,
    "image_path": output_path,
    "generation_time": round(generation_time, 2)
}