# MITRE ATT&CK TOP Techniques Analyzer
This script is designed to analyze the MITRE ATT&CK enterprise techniques and provide a top list based on their occurrences across various threat groups and malware. Logic behind the script:
1.Fetching Data: The script starts by making a request to the MITRE ATT&CK groups and software URL.
2.Downloading Techniques: For each threat group & malware, the script identifies and downloads the associated JSON files which contain the techniques ID.
3.Analyzing Techniques: The script parses each file to count the occurrences of each technique across all the downloaded pages and sorts them. Output example:

![MicrosoftTeams-image](https://github.com/semelnyk/mittreATTACK/assets/97104452/8e0153ba-0a09-4007-b530-b8a2767b127b)

