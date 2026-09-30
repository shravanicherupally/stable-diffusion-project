from clip_evaluator import calculate_clip_similarity


image_path = "generated_images/original_prompt_image.png"

prompt = "a girl in a forest"


print("\n========================================")
print("     ORIGINAL PROMPT EVALUATION")
print("========================================")

print("\nPrompt:")
print(prompt)

print("\nCalculating CLIP similarity...")
print("Please wait...")

score = calculate_clip_similarity(
    image_path,
    prompt
)

print("\n========================================")
print("             RESULT")
print("========================================")

print(f"CLIP Similarity Score: {score:.4f}")