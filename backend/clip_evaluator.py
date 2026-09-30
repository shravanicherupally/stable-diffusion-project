import torch
from PIL import Image
from transformers import CLIPProcessor, CLIPModel


# CLIP model
MODEL_ID = "openai/clip-vit-base-patch32"


print("Loading CLIP model...")

# Use CPU
device = "cpu"

# Load CLIP model
model = CLIPModel.from_pretrained(MODEL_ID)
processor = CLIPProcessor.from_pretrained(MODEL_ID)

model = model.to(device)


def calculate_clip_similarity(image_path, prompt):

    image = Image.open(image_path).convert("RGB")

    inputs = processor(
        text=[prompt],
        images=image,
        return_tensors="pt",
        padding=True
    )

    inputs = {
        key: value.to(device)
        for key, value in inputs.items()
    }

    with torch.no_grad():

        image_output = model.get_image_features(
            pixel_values=inputs["pixel_values"]
        )

        text_output = model.get_text_features(
            input_ids=inputs["input_ids"],
            attention_mask=inputs["attention_mask"]
        )

        # Transformers may return a model-output object
        # instead of a tensor.
        image_features = (
            image_output.pooler_output
            if hasattr(image_output, "pooler_output")
            else image_output
        )

        text_features = (
            text_output.pooler_output
            if hasattr(text_output, "pooler_output")
            else text_output
        )

    # Normalize embeddings
    image_features = image_features / image_features.norm(
        dim=-1,
        keepdim=True
    )

    text_features = text_features / text_features.norm(
        dim=-1,
        keepdim=True
    )

    # Calculate cosine similarity
    similarity = (
        image_features @ text_features.T
    ).item()

    return similarity


if __name__ == "__main__":

    image_path = "generated_images/generated_api_image.png"

    prompt = (
        "a girl in a forest, highly detailed, beautiful composition, "
        "cinematic lighting, sharp focus, professional photography, "
        "high quality"
    )

    print("\nCalculating CLIP similarity...")
    print("Please wait...")

    score = calculate_clip_similarity(
        image_path,
        prompt
    )

    print("\n===== CLIP EVALUATION =====")
    print(f"Prompt: {prompt}")
    print(f"CLIP Similarity Score: {score:.4f}")