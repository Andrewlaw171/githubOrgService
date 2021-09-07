import unittest
from app.config.config import githubMember
from app.handlers.utils import GithubUtils


class TestApi(unittest.TestCase):
    def test_get_highest_follow_count(self):
        member_list = [
            githubMember("Andrew", 1),
            githubMember("Adam", 25),
            githubMember("Guy", 999999)
        ]

        github_utils = GithubUtils()

        github_utils.members = member_list
        assert github_utils.get_highest_follower_count() == 'Guy'


if __name__ == '__main__':
    unittest.main()
