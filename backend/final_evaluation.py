from clip_evaluator import calculate_clip_similarity


# ==============================
# ORIGINAL PROMPT EXPERIMENT
# ==============================

original_image = "generated_images/original_prompt_image.png"

original_prompt = "a girl in a forest"


# ==============================
# ENHANCED PROMPT EXPERIMENT
# ==============================

enhanced_image = "generated_images/generated_api_image.png"

enhanced_prompt = (
    "a girl in a forest, highly detailed, "
    "beautiful composition, cinematic lighting, "
    "sharp focus, professional photography, "
    "high quality"
)


print("\n========================================")
print("       FINAL PROMPT EVALUATION")
print("========================================")


print("\nEvaluating ORIGINAL prompt image...")
original_score = calculate_clip_similarity(
    original_image,
    original_prompt
)


print("\nEvaluating ENHANCED prompt image...")
enhanced_score = calculate_clip_similarity(
    enhanced_image,
    enhanced_prompt
)


difference = enhanced_score - original_score


print("\n========================================")
print("          FINAL RESULTS")
print("========================================")


print("\nOriginal Prompt:")
print(original_prompt)

print(f"Original CLIP Score: {original_score:.4f}")


print("\nEnhanced Prompt:")
print(enhanced_prompt)

print(f"Enhanced CLIP Score: {enhanced_score:.4f}")


print("\n========================================")
print("             COMPARISON")
print("========================================")


print(f"Original Score : {original_score:.4f}")
print(f"Enhanced Score: {enhanced_score:.4f}")
print(f"Difference    : {difference:.4f}")


print("\n========================================")
print("          EXPERIMENT COMPLETE")
print("========================================")