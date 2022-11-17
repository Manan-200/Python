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
    file = json.dumps(DATA_FILE)
    client.sendall(bytes(file, encoding="utf-8"))

def receive():
    print(client.recv(2048).decode(FORMAT))

while True:
    send_file()
    thread = threading.Thread(target=receive)