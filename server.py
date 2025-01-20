import socket
import threading
import datetime

# Dictionary to keep track of connected clients and their names
clients = {}
PORT = 1234

# Function to handle individual client connections
def handle_client(client_socket, client_address):
    # Receive the client's name
    client_name = client_socket.recv(1024).decode('utf-8')
    clients[client_name] = client_socket
    print(f'{client_name} connected from {client_address}')

    # Notify all clients that a new client has joined
    broadcast_message(f"{client_name} has joined the chat.")

    try:
        while True:
            # Receive messages from the client
            message = client_socket.recv(1024)
            if not message:
                break  # Client disconnected

            message = message.decode('utf-8')
            broadcast_message(f"{client_name}: {message}")

    except Exception as e:
        print(f"Error with {client_name}: {e}")

    # If the client disconnects, remove them from the clients dictionary
    print(f'{client_name} disconnected')
    del clients[client_name]
    client_socket.close()

    # Notify everyone that the client has left
    broadcast_message(f"{client_name} has left the chat.")


# Function to broadcast messages to all connected clients
def broadcast_message(message):
    for client_name, client_socket in clients.items():
        try:
            t = datetime.datetime.now()
            t = t.strftime('%H:%M:%S')
            print(t + " - " + message)

            client_socket.send(message.encode('utf-8'))
        except Exception as e:
            print(f"Error sending message to {client_name}: {e}")


# Function to start the server
def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', PORT))  # Bind to all available IPs on port 12345
    server_socket.listen(5)

    print("Server started, waiting for clients...")

    while True:
        client_socket, client_address = server_socket.accept()
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()


if __name__ == "__main__":
    start_server()
