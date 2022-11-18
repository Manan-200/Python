import socket
import json
import threading

DATA_FILE = "client_data.json"
HEADER = 1024
PORT = 5065
FORMAT = "utf-8"

with open("ip_adr.json") as f:
    SERVER = json.load(f)["IP"]
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def save_data(file, data):
    with open(file, "w") as f:
        json.dump(data, f)

def load_data(file):
    try:
        with open(file, "r") as f:
            return(json.load(f))
    except:
        return {}

def send_file():
    data = load_data(DATA_FILE)
    client.send(str(data["self"]).encode(FORMAT))

def receive():
    data = load_data(DATA_FILE)
    msg = eval(client.recv(2048).decode(FORMAT))
    data.update(msg)
    save_data(DATA_FILE, data)

n = 0
while True:
    n += 1
    if n % 1000 == 0:
        send_file()
    thread = threading.Thread(target=receive)
    thread.start()