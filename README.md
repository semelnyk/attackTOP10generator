# MITRE ATT&CK TOP Techniques Analyzer
This script is designed to analyze the MITRE ATT&CK enterprise techniques and provide a top list based on their occurrences across various threat groups and malware. Logic Behind the Script:
- Fetching Data: The script starts by making a request to the MITRE ATT&CK groups and software URL.
- Downloading Techniques: For each threat group & malware, the script identifies and downloads the associated JSON files which contain the techniques ID.
- Analyzing Techniques: Once all the files are downloaded, the script parses each file to count the occurrences of each technique across all the downloaded pages. Output example:

![MicrosoftTeams-image](https://github.com/semelnyk/mittreATTACK/assets/97104452/8e0153ba-0a09-4007-b530-b8a2767b127b)

