import json
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def load_data(file_name):
    with open(file_name, 'r') as file:
        return json.load(file)

def create_github_issue(title, description, url, headers):
    issue_data = {'title': title, 'body': description}
    response = requests.post(url, headers=headers, json=issue_data)
    if response.status_code == 201:
        print(f"Issue '{title}' created successfully.")
    else:
        print(f"Failed to create issue '{title}'. Response: {response.text}")

def main():
    data = load_data('data.json')
    token = os.getenv('GITHUB_TOKEN')
    repo = os.getenv('GITHUB_REPO')

    if not token or not repo:
        print("GitHub token and repo must be set in the environment.")
        return

    url = f'https://api.github.com/repos/{repo}/issues'
    headers = {'Authorization': f'token {token}', 'Accept': 'application/vnd.github.v3+json'}

    for item in data:
        create_github_issue(item['title'], item['description'], url, headers)

if __name__ == "__main__":
    main()
