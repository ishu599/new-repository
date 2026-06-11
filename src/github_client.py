import requests

class GitHubClient:
    def __init__(self, token):
        self.token = token
    
    def get_repo_info(self, repo):
        url = f"https://api.github.com/repos/{repo}"

       

        response = requests.get(url)

        response.raise_for_status()
        return response.json()