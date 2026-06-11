print("Program started")

import os
from github_client import GitHubClient
from report_generator import build_report
from slack_notifier import send_to_slack
from datetime import datetime
def main():

    github_token = os.getenv("GITHUB_TOKEN")
    

    repo = "boto/boto3"

    github = GitHubClient(github_token)

    repo_data = github.get_repo_info(repo)
    print("fetching github data ")
    print(repo_data)
    report =  build_report(repo_data)
    print("generating report")
    print(report)

    print(report)
    timestamp = datetime.utcnow().strftime(
        "%Y-%m-%d %H:%M:%S UTC"
    )

    report = f"# Generated on {timestamp}\n\n{report}"

    os.makedirs("reports", exist_ok=True)

    with open(
        "reports/github-health-report.md",
        "w",
        encoding="utf-8"
    ) as file:
        file.write(report)

    
    print ("sending to slack")
if __name__ == "__main__":
    main()