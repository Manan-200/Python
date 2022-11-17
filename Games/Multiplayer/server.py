import socket
import threading
import json

data = {}

def save_data(file, data):
    with open(file, "w") as f:
        json.dump(data, f)

DATA_FILE = "server_data.json"
HEADER = 1024
PORT = 5065
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = "utf-8"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"{addr} hopped in!")
    connected = True

    while connected:
        msg = conn.recv(HEADER).decode(FORMAT)
        data[f"{addr}"] = msg
        save_data(DATA_FILE, data)
        #conn.send(json.dumps(DATA_FILE))
        conn.send("data received".encode(FORMAT))

    conn.close()

def start():
    server.listen()
    print(f"ip: {SERVER}")
    while True:
        conn, adrr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, adrr))
        thread.start()
        print(f"[ACTIVE CONNECTION] {threading.active_count() - 1}")

start()