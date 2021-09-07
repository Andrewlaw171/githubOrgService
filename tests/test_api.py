import unittest
import requests

from app.config.config import GithubMember
from app.handlers.utils import GithubUtils
from unittest.mock import patch, Mock
from tests.test_data import TestMemberListResponse


class TestApi(unittest.TestCase):
    def test_populate_members(self):
        with unittest.mock.patch.object(
                requests, 'get', return_value=Mock(status_code=200, json=lambda: TestMemberListResponse.TEST_MEMBER_LIST)
        ):
            github_utils = GithubUtils("test")

            github_utils.get_member_follower_count = Mock()
            github_utils.get_member_follower_count.side_effect = [1, 2, 3, 4, 5]

            github_utils.populate_members()

            assert github_utils.members[0].github_id == 4426
            assert github_utils.members[1].github_id == 1235045
            assert github_utils.members[2].github_id == 790027
            assert github_utils.members[3].github_id == 1724585
            assert github_utils.members[4].github_id == 11731882

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
