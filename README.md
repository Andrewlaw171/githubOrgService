# githubOrgService
githubOrgService is a flask application that provides a REST API for users to return the member of a Github organization with the highest number of followers.

### Running Locally

1. Create a new venv `python3 -m venv venv` and `pip install -r requirements.txt` (Note: This app was developed on Python3.9 and it is the recommended version)
2. Edit the run configuration of app.py to include your github access token in `ACCESS_TOKEN=<access_token>`
3. Run app.py in your ide

### Usage
`GET /highest_follow_count/{organization}`

Retrieves the username and follower count of the member with the highest number of followers in the organization

### Deployment
Proposed deployment would involve the following workflow:
1. Jenkins job pulls source code from master branch, packages code into wheel format and pushes package to python package repo
2. Ansible job pulls updated python package, configures env access_token and systemd unit for running api server on remote server

### Risks
The current authentication method relies on personal access tokens which are not recommended for production deployment and might pose a minor security risk

There is no rate limiter on this api so it is possible for users to spam the endpoint thus consuming the github api rate limit allocation.

There is no authentication configured around accessing this api. Therefore if this app were to be deployed on the internet anyone could access it.
