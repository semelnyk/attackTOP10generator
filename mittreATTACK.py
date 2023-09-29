import os
import requests
import re
import json
from collections import defaultdict

# Step 1: Downloading all MITRE technique .json files
base_urls = [
    "https://attack.mitre.org/versions/v13/groups/",
    "https://attack.mitre.org/versions/v13/software/"
]
output_directory = "enterprise_layers"

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

download_count = 0

for base_url in base_urls:
    response = requests.get(base_url)
    if response.status_code == 200:
        js_code = response.text
        pattern = r'(?<=href=")(/versions/v13/(?:groups|software)/[A-Z0-9]+/)'
        item_urls = re.findall(pattern, js_code)

        for item_url in item_urls:
            item_page_url = "https://attack.mitre.org" + item_url
            item_response = requests.get(item_page_url)

            if item_response.status_code == 200:
                item_page_content = item_response.text
                json_pattern = r'(?<=href=")(/versions/v13/(?:groups|software)/[A-Z0-9]+/[A-Z0-9]+-enterprise-layer\.json)'
                json_urls = re.findall(json_pattern, item_page_content)

                for json_url in json_urls:
                    json_file_url = "https://attack.mitre.org" + json_url
                    json_file_name = json_url.split("/")[-1]
                    json_file_path = os.path.join(output_directory, json_file_name)

                    response = requests.get(json_file_url)

                    if response.status_code == 200:
                        with open(json_file_path, "wb") as f:
                            f.write(response.content)
                        print("Downloaded:", json_file_path)
                        download_count += 1
                    else:
                        print(f"Failed to download: {json_file_url}")
            else:
                print(f"Failed to retrieve item page: {item_page_url}")
    else:
        print(f"Failed to retrieve the list of item pages for {base_url}")

print(f"Total JSON files downloaded: {download_count}")

# Step 2 & 3: Parse downloaded files and count technique occurrences
technique_counts = defaultdict(int)

for filename in os.listdir(output_directory):
    if filename.endswith(".json"):
        with open(os.path.join(output_directory, filename), 'r') as file:
            data = json.load(file)

            if isinstance(data, list):
                technique_ids = [item.get('techniqueID') for item in data if item.get('techniqueID')]
            elif isinstance(data, dict):
                techniques = data.get('techniques', [])
                technique_ids = [tech.get('techniqueID') for tech in techniques if tech.get('techniqueID')]
            else:
                technique_ids = []

            for tid in technique_ids:
                technique_counts[tid] += 1

# Sort by occurrence and print
sorted_techniques = sorted(technique_counts.items(), key=lambda x: x[1], reverse=True)

sequence_number = 1
for technique, count in sorted_techniques:
    print(f"{sequence_number}. {technique}: {count}")
    sequence_number += 1
