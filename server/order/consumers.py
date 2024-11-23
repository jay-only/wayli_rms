import json
from channels.generic.websocket import AsyncWebsocketConsumer

class KitchenOrderConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Join room group
        self.room_group_name = "kitchen_order_group"
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        order_data = text_data_json['order_data']

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'kitchen_order_update',
                'order_data': order_data
            }
        )

    # Receive message from room group
    async def kitchen_order_update(self, event):
        order_data = event['order_data']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'order_data': order_data
        }))
