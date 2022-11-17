import socket
import json

HEADER = 8
PORT = 5065
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!disconnect"

with open("ip_adr.json") as f:
    SERVER = json.load(f)["IP"]
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    while msg != "":
        sel_msg = msg[:HEADER]
        client.send(sel_msg.encode(FORMAT))
        msg = msg[len(sel_msg):]
    client.send("MsgBreak".encode(FORMAT))
    print(client.recv(2048).decode(FORMAT))

state = True
while state:
    msg = input("Enter the msg: ")
    send(msg)