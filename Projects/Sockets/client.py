import socket
import json

HEADER = 64
PORT = 5050
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!disconnect"

with open("ip_adr.json") as f:
    SERVER = json.load(f)["IP"]
SERVER = "192.168.94.23"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_len = len(message)
    send_len = str(msg_len).encode(FORMAT)
    send_len += b"" * (HEADER - len(send_len))
    client.send(send_len)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

for i in range(int(input("Enter number of messages: "))):
    send(input("Enter the message: "))
send(DISCONNECT_MESSAGE)