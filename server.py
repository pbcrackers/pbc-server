import falcon
import multiprocessing
import pbc.game

from dotenv import load_dotenv
from pathlib import Path

class AnswerResource(object):
    def on_get(self, req, res):
        """Handles all get requests"""
        res.status = falcon.HTTP_200
        res.body = ('Hello, world!')

class StartGameResource(object):
    def on_get(self, req, res):
        """Start the game"""
        game = pbc.game.Game()
        game_proc = multiprocessing.Process(target = game.run, args =())
        game_proc.start()
        res.status = falcon.HTTP_200
        res.body = ('Game started')


app = falcon.API()
app.add_route('/answer', AnswerResource())
app.add_route('/start', StartGameResource())

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path, verbose=True)
