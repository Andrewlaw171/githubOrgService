import unittest
from app.config.config import GithubMember
from app.handlers.utils import GithubUtils


class TestApi(unittest.TestCase):
    def test_populate_members(self):
        github_utils = GithubUtils("MYOB-Technology")
        github_utils.populate_members()

    def test_get_highest_follow_count(self):
        member_list = [
            GithubMember('1', "Andrew", 1),
            GithubMember('2', "Adam", 25),
            GithubMember('3', "Guy", 999999)
        ]

        github_utils = GithubUtils('test')

        github_utils.members = member_list
        assert github_utils.get_highest_follower_count() == '3'


if __name__ == '__main__':
    unittest.main()
