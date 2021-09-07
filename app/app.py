from flask import Flask
app = Flask(__name__)


@app.route('/highest_follow_count')
def get_highest_follow_count():
    return 'test'
