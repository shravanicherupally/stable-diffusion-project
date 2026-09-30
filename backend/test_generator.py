from generator import generate_image


# Test prompt
prompt = "a girl in a forest"

output_path = generate_image(
    prompt,
    filename="original_prompt_image.png"
)


print("\nGeneration completed!")
print(f"Image saved at: {output_path}")