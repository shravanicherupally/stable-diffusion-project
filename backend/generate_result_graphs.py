import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Project paths
BASE_DIR = Path(__file__).resolve().parent.parent
RESULTS_DIR = BASE_DIR / "results"

csv_path = RESULTS_DIR / "FINAL_MASTER_RESULTS.csv"

# Load results
df = pd.read_csv(csv_path)

print("Results loaded successfully:")
print(df)

# --------------------------------------------------
# 1. Model Comparison - CLIP Score
# --------------------------------------------------

model_df = df[df["Experiment"] == "Model Comparison"]

plt.figure(figsize=(8, 5))

plt.bar(
    model_df["Model"],
    model_df["CLIP Similarity"]
)

plt.title("Model Comparison using CLIP Score")
plt.xlabel("Model")
plt.ylabel("CLIP Score")
plt.xticks(rotation=15)
plt.tight_layout()

model_graph = RESULTS_DIR / "model_comparison_clip.png"
plt.savefig(model_graph, dpi=300)
plt.close()

print(f"\nSaved: {model_graph}")


# --------------------------------------------------
# 2. Prompt Engineering - CLIP Score
# --------------------------------------------------

prompt_df = df[df["Experiment"].str.contains("Prompt Engineering")]

plt.figure(figsize=(8, 5))

labels = (
    prompt_df["Experiment"]
    + " - "
    + prompt_df["Prompt Type"]
)

plt.bar(
    labels,
    prompt_df["CLIP Similarity"]
)

plt.title("Prompt Engineering Comparison using CLIP Score")
plt.xlabel("Experiment")
plt.ylabel("CLIP Score")
plt.xticks(rotation=20)
plt.tight_layout()

prompt_graph = RESULTS_DIR / "prompt_engineering_clip.png"
plt.savefig(prompt_graph, dpi=300)
plt.close()

print(f"Saved: {prompt_graph}")

print("\n========================================")
print("EVALUATION GRAPHS CREATED SUCCESSFULLY")
print("========================================")