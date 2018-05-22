import os
import pusher
import json
import yaml
import time

class Game:

    def __init__(self):
        self.pusher_client = pusher.Pusher(
            app_id=os.getenv("PUSHER_APP_ID"),
            key=os.getenv("PUSHER_KEY"),
            secret=os.getenv("PUSHER_SECRET"),
            cluster=os.getenv("PUSHER_CLUSTER"),
            ssl=True
        )

        with open("questions.yaml", 'r') as stream:
            try:
                self.questions = yaml.safe_load(stream)['questions']
                print(self.questions)
            except yaml.YAMLError as e:
                print("Failed to parse questions file")
                print(e)
                exit

    def run(self):
        print("asking questions")
        for q in self.questions:
            print('asking question ' + q['question'])
            self.pusher_client.trigger(
                'questions', 'ask-question',
                json.dumps({
                    'question': q['question'],
                    'answers': q['answers']
                }))
            time.sleep(30)