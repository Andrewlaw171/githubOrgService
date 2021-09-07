import requests

from src.config.config import GithubMember
from operator import attrgetter


class GithubUtils(object):
    def __init__(self, organisation):
        self.organisation = organisation
        self.members = []

    def get_member_follower_count(self, username):
        return requests.get("https://api.github.com/users/" + username).json()['followers']

    def populate_members(self):
        organisation_members = requests.get("https://api.github.com/orgs/" + self.organisation + "/members").json()

        for member in organisation_members:
            username = member['login']
            github_id = member['id']

            follower_count = self.get_member_follower_count(username)

            self.members.append(GithubMember(github_id, username, follower_count))

    def get_highest_follower_count(self):
        highest_followed_member = max(self.members, key=attrgetter('follower_count'))

        return highest_followed_member
