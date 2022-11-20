import socket
import threading
import json

DATA_FILE = "server_data.json"
HEADER = 1024
PORT = 5065
#SERVER = socket.gethostbyname(socket.gethostname())
SERVER = "0.0.0.0"
ADDR = (SERVER, PORT)
FORMAT = "utf-8"

def load_data(file):
    try:
        with open(file, 'r') as f:
            return(json.load(f))
    except:
        return {}

def save_data(file, data):
    with open(file, "w") as f:
        json.dump(data, f)

save_data(DATA_FILE, {})

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"{addr} hopped in!")
    connected = True

    while connected:
        msg = conn.recv(HEADER).decode(FORMAT)
        if msg == "!":
            connected = False
        else:
            msg = eval(msg)
            data = load_data(DATA_FILE)
            if f"{addr}" not in data:
                data[f"{addr}"] = msg
                save_data(DATA_FILE, data)
            else:
                if data[f"{addr}"] != msg:
                    data[f"{addr}"] = msg
                    save_data(DATA_FILE, data)

            sending_data = {}
            for key in data:
                if key != str(addr):
                    sending_data[key] = data[key]
            conn.send(str(sending_data).encode(FORMAT))
    print(f"{addr} left the server")
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