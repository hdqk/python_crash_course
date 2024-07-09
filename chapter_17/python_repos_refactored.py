import requests


def check_response():
    # Make an API call and check the response.
    url = "https://api.github.com/search/repositories"
    url += "?q=language:python+sort:stars+stars:>10000"
    headers = {"Accept": "application/vnd.github.v3+json"}
    r = requests.get(url, headers=headers)
    return r


def check_status_code(response):
    print(f"Status code: {response.status_code}")


def convert_repo_dict(response):
    # Convert the response object to a dictionary.
    response_dict = response.json()
    return response_dict


def print_results(response_dict):
    print(f"Total repos: {response_dict['total_count']}")
    print(f"Complete results: {not response_dict['incomplete_results']}")
    repo_dicts = response_dict['items']
    print(f"Repos returned: {len(repo_dicts)}")


response = check_response()
check_status_code(response)
response_dict = convert_repo_dict(response)
print_results(response_dict)
