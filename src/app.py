import logging
import os

from flask import Flask, jsonify
from src.handlers.utils import GithubUtils


def create_app():
    app = Flask(__name__)
    app.config['JSON_SORT_KEYS'] = False
    logger = logging.getLogger(__name__)
    access_token = os.environ['ACCESS_TOKEN']

    @app.route('/highest_follow_count/<organisation>')
    def highest_follow_count(organisation):
        github_utils = GithubUtils(organisation, access_token)

        try:
            github_utils.populate_members()
        except RuntimeError as err:
            logger.warning(err.args[0])
            return err.args[0], err.args[1]

        if not github_utils.members:
            return "No members found in organisation", 404

        member = github_utils.get_highest_follower_count()
        return jsonify({"username": member.name, "followers": member.follower_count})

    return app


# For debugging purposes, only used when running locally (i.e. through pycharm)
if __name__ == "__main__":
    local_app = create_app()
    local_app.run(host='127.0.0.1', port=4390)

