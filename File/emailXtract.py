import re
import requests

def extract_emails_from_webpage(url):
    # Fetch the webpage content
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to fetch the webpage: {url}")
        return []

    # Use a regular expression to find email patterns
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(email_pattern, response.text)

    return emails


webpage_url = "https://hunter.io/"  # Replace this with the URL of the webpage you want to extract emails from
extracted_emails = extract_emails_from_webpage(webpage_url)
print("Extracted emails:")
print(extracted_emails)