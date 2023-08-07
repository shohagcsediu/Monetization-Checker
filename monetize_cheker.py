import requests
import re

# Replace this with the URL of the webpage you want to fetch
channel_url = 'MoShohag'
url = "https://www.youtube.com/@" + channel_url

# Send a GET request to the URL to fetch the HTML content
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Get the HTML content of the page
    html_content = response.text
    
    # Define the pattern for the JSON-like structure
    pattern = r'{"key":"is_monetization_enabled","value":"(true|false)"}'
    
    # Search for the pattern in the HTML content
    matches = re.findall(pattern, html_content)
    
    if matches:
        for match in matches:
            print(f"Found match: {match}")
    else:
        print("No matches found.")
else:
    print("Failed to fetch the webpage.")