from clip_evaluator import calculate_clip_similarity


# Existing generated image
image_path = "generated_images/generated_api_image.png"


# Original prompt
original_prompt = "a girl in a forest"


# Enhanced prompt
enhanced_prompt = (
    "a girl in a forest, highly detailed, "
    "beautiful composition, cinematic lighting, "
    "sharp focus, professional photography, "
    "high quality"
)


print("\n========================================")
print("     PROMPT ENGINEERING EVALUATION")
print("========================================")


print("\nCalculating CLIP score for ORIGINAL prompt...")
original_score = calculate_clip_similarity(
    image_path,
    original_prompt
)


print("\nCalculating CLIP score for ENHANCED prompt...")
enhanced_score = calculate_clip_similarity(
    image_path,
    enhanced_prompt
)


print("\n========================================")
print("          COMPARISON RESULTS")
print("========================================")

print(f"\nOriginal Prompt:")
print(original_prompt)

print(f"CLIP Score: {original_score:.4f}")


print(f"\nEnhanced Prompt:")
print(enhanced_prompt)

print(f"CLIP Score: {enhanced_score:.4f}")


print("\n========================================")
print("             DIFFERENCE")
print("========================================")

difference = enhanced_score - original_score

print(f"Score Difference: {difference:.4f}")