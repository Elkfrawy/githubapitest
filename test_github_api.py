import github_api


def test_get_repos_should_return_valid_list():
    repos = github_api.get_user_repos_list('Elkfrawy')
    assert len(repos) > 0
    assert "AnimatedProfile" in repos
    assert "githubapitest" in repos


def test_get_repos_return_empty_list_with_invalid_name():
    repos = github_api.get_user_repos_list('asfas9gast306236kdt89236dghd')
    assert len(repos) == 0


def test_get_repos_count_return_positive_number():
    repo_count = github_api.get_repo_commits_count('Elkfrawy', 'AnimatedProfile')
    assert repo_count > 0


def test_get_not_found_repos_count_return_zero():
    repo_count = github_api.get_repo_commits_count('Elkfrawy', 'aabbccdd61236216')
    assert repo_count == 0


def test_get_repo_not_found_user_return_zero():
    repo_count = github_api.get_repo_commits_count('asfas9gast306236kdt89236dghd', 'AnimatedProfile')
    assert repo_count == 0


def test_user_repos_commits_return_valid_list():
    repos = github_api.user_repositories_commits('Elkfrawy')
    assert repos
    assert 'Repo: AnimatedProfile Number of commits: 5' in repos
    assert 'githubapitest' in repos


def test_user_repos_commits_return_empty_string_with_invalid_user():
    repos = github_api.user_repositories_commits('asfas9gast306236kdt89236dghd')
    assert not repos