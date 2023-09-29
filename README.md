# MITRE ATT&CK TOP Techniques Analyzer
This script is designed to analyze the MITRE ATT&CK enterprise techniques and provide a top list based on their popularity or occurrences across various threat groups and malware. By analyzing data from the ATT&CK database, the tool aims to highlight the most frequently employed techniques, offering a perspective on common strategies used in the cybersecurity threat landscape.

Logic Behind the Script:
- Fetching Data: The script starts by making a request to the MITRE ATT&CK groups and software URL. This is where it retrieves the list of threat groups and malware.
- Downloading Techniques: For each threat group & malware, the script identifies and downloads the associated JSON files which contain the techniques ID.
- Analyzing Techniques: Once all the files are downloaded, the script parses each file to count the occurrences of each technique across all the downloaded pages. This data is then sorted in descending order based on the number of occurrences, and displayed to the console.

Requirements:
- Python 3.x
- requests library

How to Run the Script:
- Clone the repository
- Navigate to the repository directory
- cd mittreATTACK

Run the script:
```
python3 mittreATTACK.py
```

This will execute the script, download the required JSON files into an enterprise_layers directory, and then analyze and display the occurrences of each technique. Output example:





<img width="399" alt="Untitled" src="https://github.com/semelnyk/mittreATTACK/assets/97104452/af0391ab-8e57-46a6-a72c-d67373e4e4aa">


