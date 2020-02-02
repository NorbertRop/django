from asgiref.sync import async_to_sync
from channels.generic.websocket import JsonWebsocketConsumer

from .kosci import Kosci

kosci = Kosci()

class GameConsumer(JsonWebsocketConsumer):

    def connect(self):
        kosci.graczDolaczyl(self)

    def disconnect(self, close_code):
        kosci.graczRozlaczyl(self)

    def receive_json(self, dane):
        if 'rzut' in dane:
            column = dane.get('rzut')
            kosci.player_click(self, column)