import asyncio
import websockets

# create handler for each connection
async def response(websocket, path):
    message = await websocket.recv()
    print(f"We got the message from the client: {message}")
    await websocket.send("I can confirm I got your message!")

start_server = websockets.serve(response, 'localhost', 8800)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()