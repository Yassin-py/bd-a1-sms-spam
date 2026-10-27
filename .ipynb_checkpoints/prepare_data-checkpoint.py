
import pandas as pd
from pathlib import Path

# Find the project folder and dataset
project_dir = Path(__file__).resolve().parent
input_file = project_dir / "data" / "SMSSpamCollection"
output_file = project_dir / "data" / "dataset.csv"

# Read the original tab-separated file
df = pd.read_csv(
    input_file,
    sep="\t",
    header=None,
    names=["label", "message"],
    encoding="utf-8"
)

# Save as CSV
df.to_csv(output_file, index=False)

# Verify the result
print("Dataset prepared successfully!")
print("Shape:", df.shape)
print(df.head())
print("\nClass distribution:")
print(df["label"].value_counts())
print("\nSaved to:", output_file)
