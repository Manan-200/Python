import socket
import threading

HEADER = 8
PORT = 5065
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!disconnect"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected. ")

    connected = True
    final_msg = ""

    while connected:
        msg = conn.recv(HEADER).decode(FORMAT)
        
        if msg == "MsgBreak":
            print(f"[{addr}] {final_msg}")
            conn.send("Msg recieved".encode(FORMAT))
            final_msg = ""
        else:
            final_msg += msg

        if final_msg == DISCONNECT_MESSAGE:
            connected = False

    conn.close()

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target = handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTION] {threading.active_count() - 1}")

print("[STARTING] server is starting... ")
start()