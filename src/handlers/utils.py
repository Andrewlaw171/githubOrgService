import requests

from src.config.config import GithubMember
from operator import attrgetter


class GithubUtils(object):
    def __init__(self, organisation, access_token):
        self.organisation = organisation
        self.members = []
        self.access_token = access_token

    def get_member_follower_count(self, username):
        return requests.get(
            "https://api.github.com/users/" + username,
            auth=('user', self.access_token)
        ).json()['followers']

    def populate_members(self):
        response = requests.get(
            "https://api.github.com/orgs/" + self.organisation + "/members",
            auth=('user', self.access_token)
        )

        if response.status_code == 403:
            raise RuntimeError("Github API rate limit exceeded", 403)

        for member in response.json():
            username = member['login']
            github_id = member['id']

            follower_count = self.get_member_follower_count(username)

            self.members.append(GithubMember(github_id, username, follower_count))

    def get_highest_follower_count(self):
        highest_followed_member = max(self.members, key=attrgetter('follower_count'))

        return highest_followed_member
