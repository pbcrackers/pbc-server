import os
import pusher
import json
import yaml
import time
from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path, verbose=True)

print('starting server')

pusher_client = pusher.Pusher(
    app_id=os.getenv("PUSHER_APP_ID"),
    key=os.getenv("PUSHER_KEY"),
    secret=os.getenv("PUSHER_SECRET"),
    cluster=os.getenv("PUSHER_CLUSTER"),
    ssl=True
)

with open("questions.yaml", 'r') as stream:
    try:
        questions = yaml.safe_load(stream)['questions']
        print(questions)
    except yaml.YAMLError as e:
        print("Failed to parse questions file")
        print(e)
        exit

for q in questions:
    print('asking question ' + q['question'])
    pusher_client.trigger(
        'questions', 'ask-question',
        json.dumps({
            'question': q['question'],
            'answers': q['answers']
        }))
    time.sleep(30)
