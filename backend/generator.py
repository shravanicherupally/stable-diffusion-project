import os
import time
import torch
from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler


MODEL_ID = "stable-diffusion-v1-5/stable-diffusion-v1-5"


print("Loading Stable Diffusion model...")


device = "cpu"


pipe = StableDiffusionPipeline.from_pretrained(
    MODEL_ID,
    torch_dtype=torch.float32
)


# Replace the default PNDM scheduler
# with DPMSolver for more stable inference
pipe.scheduler = DPMSolverMultistepScheduler.from_config(
    pipe.scheduler.config
)


# Move the model to CPU
pipe = pipe.to(device)


def generate_image(prompt, filename="generated_image.png"):
    """
    Generate an image from a text prompt.

    Parameters:
        prompt   : Text description entered by the user
        filename : Name of the generated image

    Returns:
        Path of the generated image and generation time
    """

    print("\nGenerating image for prompt:")
    print(prompt)

    # Start timer
    start_time = time.time()

    image = pipe(
    prompt,
    height=512,
    width=512,
    num_inference_steps=5,
    guidance_scale=7.5
).images[0]

    output_folder = "generated_images"

    os.makedirs(
        output_folder,
        exist_ok=True
    )

    output_path = os.path.join(
        output_folder,
        filename
    )

    # Save image
    image.save(output_path)

    # Calculate generation time
    generation_time = time.time() - start_time

    print(
        f"Image saved successfully: {output_path}"
    )

    print(
        f"Generation time: {generation_time:.2f} seconds"
    )

    return output_path, generation_time