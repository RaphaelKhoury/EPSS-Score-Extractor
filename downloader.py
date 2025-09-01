import os
import requests
from datetime import date, timedelta

# Configuration
SAVE_DIR = "epss_data"       # Local folder to store files
START_DATE = date(2021, 4, 14)  # EPSS daily files started around June 2021
END_DATE = date.today()        # Up to current date
BASE_URL = "https://epss.empiricalsecurity.com/epss_scores-{:%Y-%m-%d}.csv.gz"

# Create folder if not exists
os.makedirs(SAVE_DIR, exist_ok=True)

# Loop through all dates
current_date = START_DATE
while current_date <= END_DATE:
    url = BASE_URL.format(current_date)
    filename = os.path.join(SAVE_DIR, f"epss_scores-{current_date:%Y-%m-%d}.csv.gz")

    # Skip if already downloaded
    if os.path.exists(filename):
        print(f"Skipping {filename} (already exists)")
    else:
        print(f"Downloading {url}...")
        response = requests.get(url)
        if response.status_code == 200:
            with open(filename, "wb") as f:
                f.write(response.content)
            print(f"Saved to {filename}")
        else:
            print(f"No file for {current_date:%Y-%m-%d} (HTTP {response.status_code})")

    current_date += timedelta(days=1)

print("Download complete.")