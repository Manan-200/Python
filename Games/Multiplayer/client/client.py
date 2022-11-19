import socket
import json
import threading

DATA_FILE = "client_data.json"
HEADER = 1024
PORT = 5065
FORMAT = "utf-8"

def save_data(file, data):
    with open(file, "w") as f:
        json.dump(data, f)

def load_data(file):
    try:
        with open(file, "r") as f:
            return(json.load(f))
    except:
        return {}

def send():
    data = load_data(DATA_FILE)
    try:
        client.send(str(data["self"]).encode(FORMAT))
    except:
        pass

def receive():
    msg = eval(client.recv(2048).decode(FORMAT))
    data = load_data(DATA_FILE)
    if len(msg) != 0:
        data.update(msg)
        save_data(DATA_FILE, data)

with open("ip_adr.json") as f:
    SERVER = json.load(f)["IP"]
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

save_data(DATA_FILE, {"self": [0, 0]})

n = 0
while True:
    n += 1
    if n % 5 == 0:
        n = 0
        send()
    thread = threading.Thread(target=receive)
    thread.start()