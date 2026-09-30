import torch
from diffusers import StableDiffusionPipeline

# Stable Diffusion model
MODEL_ID = "stable-diffusion-v1-5/stable-diffusion-v1-5"

print("Loading Stable Diffusion model...")
print("The first run will download the model.")
print("This may take some time.")

# Your computer does not have an NVIDIA CUDA GPU,
# so we are using the CPU.
device = "cpu"

# Load the Stable Diffusion pipeline
pipe = StableDiffusionPipeline.from_pretrained(
    MODEL_ID,
    torch_dtype=torch.float32
)

# Move the model to CPU
pipe = pipe.to(device)

# Prompt
prompt = "A beautiful mountain landscape with snow-covered mountains, a clear blue lake, green trees, blue sky, cinematic landscape photography"

print("\nGenerating image...")
print("Please wait. CPU generation can take several minutes.")

# Generate image
image = pipe(
    prompt,
    height=512,
    width=512,
    num_inference_steps=20,
    guidance_scale=7.5
).images[0]

# Save the generated image
output_path = "generated_image.png"
image.save(output_path)

print("\nImage generated successfully!")
print(f"Saved as: {output_path}")