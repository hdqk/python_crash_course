import python_repos_refactored as pyrepo
import pytest


def test_status_code():
    assert pyrepo.check_response().status_code == 200


def test_total_repos():
    r = pyrepo.check_response()
    response_dict = pyrepo.convert_repo_dict(r)
    assert response_dict['total_count'] >= 100
