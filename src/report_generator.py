def build_report(repo_data):
    report = f"""

Repository: {repo_data['full_name']}

Starts: {repo_data['stargazers_count']}
Forks: {repo_data['forks_count']}
Open Issues: {repo_data['open_issues_count']}
Language: {repo_data['language']}

Reposity URL:
{repo_data['html_url']}
"""

    return report