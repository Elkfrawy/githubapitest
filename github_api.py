import requests
import json


def user_repositories_commits(user_id):
    result = []
    repos = get_user_repos_list(user_id)
    for repo in repos:
        commits_count = get_repo_commits_count(user_id, repo)
        result.append("Repo: {} Number of commits: {}".format(repo, commits_count))
    return '\n'.join(result)


def get_user_repos_list(user_id):
    repos_url = "https://api.github.com/users/{}/repos".format(user_id)
    repos = get_and_parse_json(repos_url)
    if type(repos) is list:
        return list(map(lambda repo: repo['name'], repos))
    else:
        return []


def get_repo_commits_count(user_id, repo_name):
    commits_url = "https://api.github.com/repos/{}/{}/commits".format(user_id, repo_name)
    commits = get_and_parse_json(commits_url)
    if type(commits) is list:
        return len(commits)
    else:
        return 0


def get_and_parse_json(request_url):
    response = requests.get(request_url)
    return json.loads(response.text)
