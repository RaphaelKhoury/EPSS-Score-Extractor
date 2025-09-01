import os
import csv

# Configuration
INPUT_DIR = "epss_unzipped"  # Folder containing unzipped CSV files
OUTPUT_FILE = "cve_values.txt"
cveN = "CVE-2021-34527"  # Replace with the desired CVE number

results = []

# Loop through all CSV files
for filename in sorted(os.listdir(INPUT_DIR)):
    if filename.endswith(".csv") and filename.startswith("epss_scores-"):
        file_path = os.path.join(INPUT_DIR, filename)

        # Extract date from filename
        date_part = filename[len("epss_scores-"):-len(".csv")]

        # Read file and search for CVE
        with open(file_path, newline='', encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if len(row) >= 2 and row[0].strip() == cveN:
                    value = row[1].strip()
                    results.append(f"{date_part}, {value}")
                    break  # Stop after first match in this file

# Write results to text file
with open(OUTPUT_FILE, "w", encoding="utf-8") as out:
    out.write("\n".join(results))

print(f"Values for {cveN} saved to {OUTPUT_FILE}")