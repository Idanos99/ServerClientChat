import socket
import threading
import datetime

PORT = 1234

# Function to receive messages from the server
def receive_messages(client_socket):
    while True:
        message = client_socket.recv(1024).decode('utf-8')
        if message:
            t = datetime.datetime.now()
            t = t.strftime('%H:%M:%S')
            print(t + " - " + message)

# Function to send messages to the server
def send_message(client_socket):
    while True:
        message = input()
        print ('\033[1A' + '\033[K', end ='')
        if message:
            client_socket.send(message.encode('utf-8'))

# Function to start the client
def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', PORT))  # Connect to the server at localhost:12345

    # Send the client's name to the server
    client_name = input("Enter your name: ")
    client_socket.send(client_name.encode('utf-8'))

    # Start two threads: one for receiving messages and another for sending messages
    threading.Thread(target=receive_messages, args=(client_socket,)).start()
    threading.Thread(target=send_message, args=(client_socket,)).start()

if __name__ == "__main__":
    start_client()
