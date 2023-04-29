import json
import websocket
import time
import requests
import base64
import os
def on_message(ws, message):
    data = json.loads(message)
    print(f"Received: {data}")
    if data["Library"] == "Unknown":
        os.system("i2cset -y 1 0x10 0x02 0x00")
        os.system("i2cset -y 1 0x10 0x03 0x00")
        os.system("i2cset -y 1 0x10 0x04 0x00")
        os.system("i2cset -y 1 0x10 0x01 0xFF")
        os.system("aplay unknown.wav")
        os.system("i2cset -y 1 0x10 0x01 0x00")
    elif data["Library"] == "VVIP":
        os.system("i2cset -y 1 0x10 0x01 0x00")
        os.system("i2cset -y 1 0x10 0x03 0x00")
        os.system("i2cset -y 1 0x10 0x04 0x00")
        os.system("i2cset -y 1 0x10 0x02 0xFF")
        os.system("aplay vvip.wav")
        os.system("i2cset -y 1 0x10 0x02 0x00")
    elif data["Library"] == "BlackList":
        os.system("i2cset -y 1 0x10 0x02 0x00")
        os.system("i2cset -y 1 0x10 0x01 0x00")
        os.system("i2cset -y 1 0x10 0x04 0x00")
        os.system("i2cset -y 1 0x10 0x03 0xFF")
        os.system("aplay blacklist.wav")
        os.system("i2cset -y 1 0x10 0x03 0x00")
    elif data["Library"] == "WhiteList":
        os.system("i2cset -y 1 0x10 0x02 0x00")
        os.system("i2cset -y 1 0x10 0x03 0x00")
        os.system("i2cset -y 1 0x10 0x01 0x00")
        os.system("i2cset -y 1 0x10 0x04 0xFF")
        os.system("aplay verified.wav")
        os.system("i2cset -y 1 0x10 0x04 0x00")
    else:
        os.system("i2cset -y 1 0x10 0x02 0x00")
        os.system("i2cset -y 1 0x10 0x03 0x00")
        os.system("i2cset -y 1 0x10 0x04 0x00")
        os.system("i2cset -y 1 0x10 0x01 0xFF")
        os.system("aplay unknown.wav")
        os.system("i2cset -y 1 0x10 0x01 0x00")
        time.sleep(0.5)
        os.system("i2cset -y 1 0x10 0x01 0xFF")
        time.sleep(0.5)
        os.system("i2cset -y 1 0x10 0x01 0x00")
    return
    
    base64Face = None
    try:
        base64Face = base64.b64encode(requests.get("http://localhost:4300"+data['Face']).content).decode("utf-8")
    except:
        base64Face = None
    data["Base64Face"] = base64Face

    base64Image = None
    try:
        base64Image = base64.b64encode(requests.get("http://localhost:4300"+data['Image']).content).decode("utf-8")
    except:
        base64Image = None
    data["base64Image"] = base64Image

    # write received data to a file
    with open(str(int(time.time()*100000)) + '.json', 'w') as f:
        json.dump(data, f, sort_keys=True, indent=4)
        f.write('\n')

def on_error(ws, error):
    print(f"Error: {error}")

def on_close(ws):
    print("Connection closed")
    # wait for 5 seconds and then try to reconnect
    time.sleep(5)
    print("Attempting to reconnect...")
    ws.connect()

def on_open(ws):
    print("Connection opened")

# replace the URL with the WebSocket server's URL
websocket_url = "ws://192.168.10.137:4300/ws/chat/new_chat/"

while True:
    try:
        ws = websocket.WebSocketApp(websocket_url,
                                    on_message=on_message,
                                    on_error=on_error,
                                    on_close=on_close)
        ws.on_open = on_open
        ws.run_forever()
    except KeyboardInterrupt:
        break
    except:
        print("Connection failed, retrying...")
        time.sleep(5)