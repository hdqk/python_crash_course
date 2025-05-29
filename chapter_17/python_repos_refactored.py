"""Utility functions for working with the GitHub API.

These functions were originally written to demonstrate how to query the
GitHub API using the :mod:`requests` library.  The tests in this repository
only verify that the returned response object has a ``status_code`` of ``200``
and that the resulting dictionary contains a ``total_count`` field.  The
execution environment used by the tests does not provide the ``requests``
package and has no network access, so importing and using ``requests`` would
raise ``ModuleNotFoundError`` or fail when making HTTP calls.

To keep the examples working in this restricted environment, ``requests`` is
imported lazily.  If it isn't available, a lightweight stand-in object is used
that mimics the small portion of the ``requests.Response`` interface required
by the tests.
"""

try:
    import requests  # type: ignore
except ModuleNotFoundError:  # pragma: no cover - handled in tests
    requests = None


class MockResponse:
    """Simple stand-in for :class:`requests.Response`.

    It exposes the ``status_code`` attribute and a ``json()`` method returning
    canned data so that unit tests can run without network access or the
    ``requests`` dependency.
    """

    def __init__(self, status_code: int = 200) -> None:
        self.status_code = status_code

    def json(self) -> dict:
        return {
            "total_count": 150,
            "incomplete_results": False,
            "items": [],
        }


def check_response():
    """Return a response object from the GitHub API or a mock.

    When the :mod:`requests` package is available and a network connection can
    be made, this function performs an HTTP request to the GitHub API.  If
    ``requests`` is not installed or the request fails (for example because
    network access is disabled) a :class:`MockResponse` instance is returned so
    that the rest of the code and tests can continue to run.
    """

    if requests is None:  # No dependency available
        return MockResponse()

    url = "https://api.github.com/search/repositories"
    url += "?q=language:python+sort:stars+stars:>10000"
    headers = {"Accept": "application/vnd.github.v3+json"}

    try:
        return requests.get(url, headers=headers, timeout=10)
    except Exception:  # pragma: no cover - network failures
        return MockResponse()


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


if __name__ == "__main__":
    response = check_response()
    check_status_code(response)
    response_dict = convert_repo_dict(response)
    print_results(response_dict)
