import asyncio
import websockets
import json

connected_clients = set()

async def handler(websocket, path):
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            data = json.loads(message)
            for client in connected_clients:
                if client != websocket:
                    await client.send(json.dumps(data))
    except websockets.exceptions.ConnectionClosed:
        connected_clients.remove(websocket)

start_server = websockets.serve(handler, "localhost", 5001)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
