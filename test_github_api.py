import github_api
from unittest.mock import Mock, patch


@patch('requests.get')
def test_get_repos_should_return_valid_list(mock_get):
    mock_get.return_value = Mock(ok=True)
    mock_get.side_effect = requests_get_mock
    repos = github_api.get_user_repos_list('Elkfrawy')
    assert len(repos) > 0
    assert 'AnimatedProfile' in repos
    assert "githubapitest" in repos
    mock_get.assert_called_once()


@patch('requests.get')
def test_get_repos_return_empty_list_with_invalid_name(mock_get):
    mock_get.return_value = Mock(ok=True)
    mock_get.side_effect = requests_get_mock
    repos = github_api.get_user_repos_list('asfas9gast306236kdt89236dghd')
    assert len(repos) == 0
    mock_get.assert_called_once()


@patch('requests.get')
def test_get_repos_count_return_positive_number(mock_get):
    mock_get.return_value = Mock(ok=True)
    mock_get.side_effect = requests_get_mock
    repo_count = github_api.get_repo_commits_count('Elkfrawy', 'AnimatedProfile')
    assert repo_count > 0
    mock_get.assert_called_once()


@patch('requests.get')
def test_get_not_found_repos_count_return_zero(mock_get):
    mock_get.return_value = Mock(ok=True)
    mock_get.side_effect = requests_get_mock
    repo_count = github_api.get_repo_commits_count('Elkfrawy', 'aabbccdd61236216')
    assert repo_count == 0
    mock_get.assert_called_once()


@patch('requests.get')
def test_get_repo_not_found_user_return_zero(mock_get):
    mock_get.return_value = Mock(ok=True)
    mock_get.side_effect = requests_get_mock
    repo_count = github_api.get_repo_commits_count('asfas9gast306236kdt89236dghd', 'AnimatedProfile')
    assert repo_count == 0
    mock_get.assert_called_once()


@patch('requests.get')
def test_user_repos_commits_return_valid_list(mock_get):
    mock_get.return_value = Mock(ok=True)
    mock_get.side_effect = requests_get_mock
    repos = github_api.user_repositories_commits('Elkfrawy')
    assert repos
    assert 'Repo: AnimatedProfile Number of commits: 2' in repos
    assert 'githubapitest' in repos
    assert mock_get.call_count == 3


@patch('requests.get')
def test_user_repos_commits_return_empty_string_with_invalid_user(mock_get):
    mock_get.return_value = Mock(ok=True)
    mock_get.side_effect = requests_get_mock
    repos = github_api.user_repositories_commits('asfas9gast306236kdt89236dghd')
    assert not repos
    mock_get.assert_called_once()


def requests_get_mock(*args, **kwargs):
    response = Mock()
    if args[0] == 'https://api.github.com/users/Elkfrawy/repos':
        response.text = '''[
          {
            "id": 58416412,
            "name": "AnimatedProfile"
          },
          {
            "id": 22764812,
            "name": "githubapitest"
           }]'''
    elif args[0] == 'https://api.github.com/repos/Elkfrawy/AnimatedProfile/commits':
        response.text = '''
[
  {
    "sha": "580d2f520ba6ce50ec3b9f8f96f27c1a1b95dd55",
    "node_id": "MDY6Q29tbWl0NTg0MTY0MTI6NTgwZDJmNTIwYmE2Y2U1MGVjM2I5ZjhmOTZmMjdjMWExYjk1ZGQ1NQ==",
    "commit": {
      "author": {
        "name": "Ayman Elkfrawy",
        "email": "elkfrawy@gmail.com",
        "date": "2016-05-10T21:58:36Z"
      }
    }
  },
   {
    "sha": "0c84882a303698b08c1201547cc5f256662ea83d",
    "node_id": "MDY6Q29tbWl0NTg0MTY0MTI6MGM4NDg4MmEzMDM2OThiMDhjMTIwMTU0N2NjNWYyNTY2NjJlYTgzZA==",
    "commit": {
      "author": {
        "name": "Ayman Elkfrawy",
        "email": "elkfrawy@gmail.com",
        "date": "2016-05-10T21:57:17Z"
      }
    }
   }
]'''
    else:
        response.text = '''
{
  "message": "Not Found",
  "documentation_url": "https://developer.github.com/v3/repos/commits/#list-commits-on-a-repository"
}'''
    return response
