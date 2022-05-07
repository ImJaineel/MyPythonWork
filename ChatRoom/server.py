from email import message
import socket
import threading

from numpy import broadcast

port = 5000

server = socket.gethostbyname(socket.gethostname())
address = (server, port)
format = "utf-8"

client, names = [], []

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(address)

def StartChat():
    print("Server is running on {}".format(address))
    server.listen()

    while True:
        conn, addr = server.accept()
        conn.send("Name".encode(format))

        name = conn.recv(1024).decode(format)

        names.append(name)
        print(f"Name is: {name}")
        broadcastMessage(f"{name} has joined the chat".encode(format))
        conn.send("Connection Successful".encode(format))

        thread = threading.Thread(target=handle, args=(conn, addr))
        thread.start()

        print(f"Active Connections: {threading.activeCount()-1}")

def handle(conn, addr):
    print(f"New Connection {addr}")
    connected = True

    while connected:
        message = conn.recv(1024)
        broadcastMessage(message)
    conn.close()

def broadcastMessage(message):
    for client in client:
        client.send(message)

StartChat()