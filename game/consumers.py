import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChessConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = "chess_room"
        await self.channel_layer.group_add(self.room_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        move = data['move']

        await self.channel_layer.group_send(
            self.room_name, {"type": "broadcast_move", "move": move}
        )

    async def broadcast_move(self, event):
        move = event['move']
        await self.send(text_data=json.dumps({"move": move}))
