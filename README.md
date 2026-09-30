# Text-to-Image Generation using Stable Diffusion

## Project Overview

This project implements a text-to-image generation system using Stable Diffusion. 
The system accepts a natural-language text prompt and generates a corresponding image.

The project also studies prompt engineering and compares Stable Diffusion 1.5 with 
Realistic Vision V5.1 using CLIP similarity scores.

## Objectives

- Generate images from natural-language text prompts.
- Use prompt engineering to improve generated image quality and semantic alignment.
- Compare different Stable Diffusion-based models.
- Evaluate generated images using CLIP similarity.
- Develop a simple web-based text-to-image generation interface.
- Use GPU acceleration through Google Colab for faster image generation.

## Technologies Used

### Frontend
- HTML5
- CSS3
- JavaScript

### Backend
- Python
- FastAPI
- Uvicorn

### Generative AI
- Stable Diffusion 1.5
- Realistic Vision V5.1
- Hugging Face Diffusers
- Transformers

### Evaluation
- CLIP Similarity
- Prompt Engineering
- Model Comparison

### Deployment / Execution
- Google Colab
- NVIDIA Tesla T4 GPU
- Cloudflare Quick Tunnel
- Visual Studio Code

## System Workflow

User Prompt
    ↓
Web Interface
    ↓
FastAPI GPU API
    ↓
Prompt Enhancement
    ↓
Realistic Vision V5.1
    ↓
Tesla T4 GPU
    ↓
Generated Image
    ↓
Web Interface

## Experiments

### 1. Model Comparison

Stable Diffusion 1.5 and Realistic Vision V5.1 were evaluated using the same
prompt, seed, resolution, inference steps, and guidance scale.

### 2. Prompt Engineering Experiment 1

Original prompt:

"a girl in a forest"

Enhanced prompt:

"a girl in a forest, photorealistic portrait, natural facial proportions,
realistic eyes, natural skin texture, individual hair strands, soft natural
lighting, 85mm DSLR photography, shallow depth of field, sharp focus,
highly detailed"

### 3. Prompt Engineering Experiment 2

Original prompt:

"a futuristic city at night"

The prompt was enhanced with photorealistic, cinematic, lighting, architecture,
reflection, and photography-related descriptions.

## Evaluation Results

### Model Comparison

| Model | CLIP Similarity |
|---|---:|
| Realistic Vision V5.1 | 0.3252 |
| Stable Diffusion 1.5 | 0.2733 |

### Prompt Engineering 1

| Prompt Type | CLIP Similarity |
|---|---:|
| Original | 0.2815 |
| Enhanced | 0.2896 |

### Prompt Engineering 2

| Prompt Type | CLIP Similarity |
|---|---:|
| Original | 0.2545 |
| Enhanced | 0.3161 |

## Results

The experiments demonstrate that prompt engineering can affect the semantic
alignment measured by CLIP similarity. The model comparison also shows a
difference in CLIP similarity between the evaluated models under the same
controlled conditions.

## Project Structure

```text
stable-diffusion-project/
│
├── backend/
│   ├── app.py
│   ├── generator.py
│   ├── evaluation.py
│   ├── final_evaluation.py
│   ├── clip_evaluator.py
│   ├── compare_prompts.py
│   ├── prompt_engineering.py
│   └── generate_result_graphs.py
│
├── frontend/
│   ├── index.html
│   ├── script.js
│   └── style.css
│
├── results/
│   ├── final_human_portrait.png
│   ├── FINAL_MASTER_RESULTS.csv
│   ├── model_comparison_clip.png
│   ├── prompt_engineering_clip.png
│   └── experiments/
│
├── venv/
└── README.md