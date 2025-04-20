import json
import os

# —— CONFIGURE THESE ——

input_file = 'yourfile.json'     # e.g. 'Records.json' or '2022_APRIL.json'
output_dir  = 'split_output'
chunk_size  = 1000               # adjust to how many records per file you want
key         = 'locations'        # or 'timelineObjects' for semantic JSON

# —— SCRIPT LOGIC ——

# Create output dir
os.makedirs(output_dir, exist_ok=True)

# Load full JSON object
with open(input_file, 'r') as f:
    data = json.load(f)

if key not in data or not isinstance(data[key], list):
    raise ValueError(f"Key '{key}' missing or not a list in {input_file}")

# Split and write
items = data[key]
for idx in range(0, len(items), chunk_size):
    chunk = { key: items[idx:idx+chunk_size] }
    fname = f'split_{idx//chunk_size + 1}.json'
    with open(os.path.join(output_dir, fname), 'w') as out:
        json.dump(chunk, out, indent=2)

print(f"Created {len(os.listdir(output_dir))} files in '{output_dir}'")
