import gzip
import shutil
import os

# Folder containing .csv.gz files
SOURCE_DIR = "epss_data"
OUTPUT_DIR = "epss_unzipped"

# Create output directory if it doesn't exist
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Loop through all .gz files
for filename in os.listdir(SOURCE_DIR):
    if filename.endswith(".csv.gz"):
        gz_path = os.path.join(SOURCE_DIR, filename)
        csv_path = os.path.join(OUTPUT_DIR, filename[:-3])  # Remove .gz

        print(f"Unzipping {gz_path} -> {csv_path}")
        with gzip.open(gz_path, "rb") as f_in:
            with open(csv_path, "wb") as f_out:
                shutil.copyfileobj(f_in, f_out)

print("All files unzipped successfully.")