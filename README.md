# Peanut Butter Crackers - Server

Server for a multiplayer quiz game, using Pusher channels. Created for the [Dev.to Pusher contest](https://dev.to/devteam/first-ever-dev-contest-build-a-realtime-app-with-pusher-4nhp).

The client component is located [here](https://github.com/pbcrackers/pbc-client);

## Prerequisites
- Python 3.6+
- Pipenv
- Pusher account

## Usage
1. Run `pipenv install` to install dependencies
2. Set the following environment variables or add them to a .env file in the project root
    1. PUSHER_APP_ID
    2. PUSHER_KEY
    3. PUSHER_SECRET
    4. PUSHER_CLUSTER
3. Once clients are connected, start the server via one of the following methods:
    1. Run `pipenv run python server.py`
    2. Run `pipenv shell` followed by `python server.py`

## Questions
Questions can be defined in a YAML file, see questions.yaml for an example