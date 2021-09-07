from flask import Flask
from app.handlers.utils import GithubUtils

def create_app():
    app = Flask(__name__)

    @app.route('/highest_follow_count/<organisation>', methods=['GET'])
    def highest_follow_count(organisation):

        return None
