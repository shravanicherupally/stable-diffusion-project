import os
import time
from PIL import Image


def evaluate_generated_image(image_path, prompt):
    """
    Evaluate a generated image using basic measurable metrics.
    """

    # Check whether image exists
    if not os.path.exists(image_path):
        return {
            "status": "failed",
            "message": "Image file not found."
        }

    # Open image
    image = Image.open(image_path)

    # Image dimensions
    width, height = image.size

    # File size
    file_size_kb = os.path.getsize(image_path) / 1024

    # Number of pixels
    total_pixels = width * height

    return {
        "status": "success",
        "prompt": prompt,
        "image_width": width,
        "image_height": height,
        "total_pixels": total_pixels,
        "file_size_kb": round(file_size_kb, 2)
    }


if __name__ == "__main__":

    image_path = "generated_images/generated_api_image.png"

    prompt = (
        "a girl in a forest, highly detailed, beautiful composition, "
        "cinematic lighting, sharp focus, professional photography, "
        "high quality"
    )

    result = evaluate_generated_image(
        image_path,
        prompt
    )

    print("\n===== IMAGE EVALUATION =====")

    for key, value in result.items():
        print(f"{key}: {value}")