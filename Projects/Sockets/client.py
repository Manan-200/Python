import socket
import json
import threading

HEADER = 8
PORT = 15456
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!disconnect"

with open("ip_adr.json") as f:
    SERVER = json.load(f)["IP"]
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def save_data(file, data):
    with open(file, "w") as f:
        json.dump(data, f)

def send(msg):
    while msg != "":
        sel_msg = msg[:HEADER]
        client.send(sel_msg.encode(FORMAT))
        msg = msg[len(sel_msg):]
    client.send("MsgBreak".encode(FORMAT))

def recieve():
    save_data("data.json", {"data":client.recv(2048).decode(FORMAT)})

state = True
while state:
    msg = input("Enter the msg: ")
    send(msg)
    thread = threading.Thread(target = recieve)
    thread.start()