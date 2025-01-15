import socket
import datetime
IP = "127.0.0.1"
PORT = 1234
client_address = (IP, PORT)
username = input("Username: ")

c_socket = socket.socket()
c_socket.connect(client_address)
c_socket.send((username + " Join").encode())
while True:
    data = c_socket.recv(1024).decode()
    print(datetime.datetime.now(), data)
    message = input("You said: ")

    if message == "/exit":
        c_socket.send((username + " Leaved").encode())
        break

    c_socket.send((username + ": " +message).encode())
c_socket.close()
