PREREQUISITES
---
- Python 3.x installed (download from https://www.python.org if you don’t already have it)


INSTRUCTIONS
---
1. Create a working folder
2. Save the splitter script to the folder
3. Copy the Google timeline JSON file into the folder
4. Change this line in the script to the name of your JSON file and save it:
          input_file = 'yourfile.json'     # e.g. 'Records.json' or '2022_APRIL.json'
6. Change the key in the script to reflect the type of Google Timeline data you have:
          key         = 'locations'        # or 'timelineObjects' for semantic JSON
     key →   'locations' (for Records.json)
             'timelineObjects' (for Takeout semantic files)
             'semanticSegments' (for newest 2025 format change)
8. Change the chunk_size if the split files are still too big:
          chunk_size  = 1000               # adjust to how many records per file you want
9. Run the script


LOCATION HISTORY FORMAT INFO
---
Records.json → https://locationhistoryformat.com/reference/records/
Semantic Location History Data → https://locationhistoryformat.com/guides/semantic-location/


