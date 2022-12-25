from channels.consumer import SyncConsumer, AsyncConsumer
from channels.exceptions import StopConsumer


class MySyncConsumer(SyncConsumer):

    def websocket_connect(self, event):    # opens connection handshake
        print("Websocket connected....", event)
        self.send({
            'type': 'websocket.accept'
        })

    def websocket_receive(self, event):     # when data is received from client
        print("Websocket received", event)

    def websocket_disconnect(self, event):  # When connection is lost or disconnecting connection
        print("Websocket disconnected")
        # raise StopConsumer()


class MyAsyncConsumer(AsyncConsumer):

    async def websocket_connect(self, event):    # opens connection handshake
        print("Websocket connected", event)
        await self.send({
            'type': 'websocket.accept'
        })

    async def websocket_receive(self, event):     # when data is received from client
        print("Websocket received", event)

    async def websocket_disconnect(self, event):  # When connection is lost or disconnecting connection
        print("Websocket disconnected", event)
