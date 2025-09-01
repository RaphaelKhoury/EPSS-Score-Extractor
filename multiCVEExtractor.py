import os
import csv

# Configuration
INPUT_DIR = "epss_unzipped"  # Folder containing unzipped CSV files
OUTPUT_FILE = "cve_values_multi.txt"
cve_list = [
    "CVE-2021-34527",
    "CVE-2021-44228",
    "CVE-2022-22965"
]  # Add more CVEs as needed

# Dictionary to store results per CVE
results = {cve: [] for cve in cve_list}

# Loop through all CSV files
for filename in sorted(os.listdir(INPUT_DIR)):
    if filename.endswith(".csv") and filename.startswith("epss_scores-"):
        file_path = os.path.join(INPUT_DIR, filename)
        date_part = filename[len("epss_scores-"):-len(".csv")]

        # Read file and search for CVEs
        with open(file_path, newline='', encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if len(row) >= 2:
                    cve_id = row[0].strip()
                    if cve_id in results:
                        value = row[1].strip()
                        results[cve_id].append(f"{date_part}, {value}")

# Write results to text file
with open(OUTPUT_FILE, "w", encoding="utf-8") as out:
    for cve in cve_list:
        out.write(f"{cve}\n")
        out.write("\n".join(results[cve]))
        out.write("\n\n")

print(f"Values for {len(cve_list)} CVEs saved to {OUTPUT_FILE}")