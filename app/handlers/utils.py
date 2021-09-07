import requests

from app.config.config import GithubMember
from operator import attrgetter


class GithubUtils(object):
    def __init__(self, organisation):
        self.organisation = organisation
        self.members = []

    def populate_members(self):
        organisation_members = requests.get("https://api.github.com/orgs/" + self.organisation + "/members")

        for member in organisation_members.json():
            username = member['login']
            github_id = member['id']

            member_details = requests.get("https://api.github.com/users/" + username)
            follower_count = member_details['followers']

            self.members.append(GithubMember(github_id, username, follower_count))

    def get_highest_follower_count(self):
        highest_followed_member = max(self.members, key=attrgetter('follower_count'))

        return highest_followed_member.github_id
