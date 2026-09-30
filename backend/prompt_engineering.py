def enhance_prompt(user_prompt):
    """
    Enhance a simple user prompt into a more detailed
    Stable Diffusion-friendly prompt.
    """

    # Remove unnecessary spaces
    user_prompt = user_prompt.strip()

    # Prompt engineering template
    enhanced_prompt = (
        f"{user_prompt}, "
        "highly detailed, "
        "beautiful composition, "
        "cinematic lighting, "
        "sharp focus, "
        "professional photography, "
        "high quality"
    )

    return enhanced_prompt