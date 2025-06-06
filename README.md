# ServerClientChat

ServerClientChat is a simple command-line chat application built with Python's `socket` and `threading` modules. It allows multiple clients to connect to a central server and exchange messages in real-time.

---

## Features

* **Real-time Messaging**: Send and receive messages instantly.
* **Multi-client Support**: Multiple users can connect to the same chat server simultaneously.
* **User Join/Leave Notifications**: Get notified when users join or leave the chat.
* **Timestamped Messages**: All messages are displayed with a timestamp.

---

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You need Python 3 installed on your system.

### Installation

No special installation steps are required beyond having Python installed. You can simply download the `server.py` and `client.py` files.

---

## How to Run

To run the chat application, you need to start the server first, and then you can connect one or more clients.

### 1. Start the Server

Open your terminal or command prompt and navigate to the directory where you saved `server.py`. Then run:

```bash
python server.py
```

You should see the message: Server started, waiting for clients...

### 2. Start Clients

Open separate terminal or command prompt windows for each client you want to connect. Navigate to the directory where you saved client.py and run:

```bash
python client.py
```

The client will prompt you to enter your name:

```bash
Enter your name:
```

## Usage
---
* Once connected, simply **type your message** in the client terminal and press **Enter** to send it.
* All messages, including your own, will appear with a **timestamp and the sender's name**.
* When a new user joins, all connected clients will see a notification like: `[HH:MM:SS] - [ClientName] has joined the chat.`
* When a user leaves, all connected clients will see a notification like: `[HH:MM:SS] - [ClientName] has left the chat.`

## Code Overview
---

### `server.py`

The server-side application is responsible for:

* **Listening for incoming client connections.**
* **Handling each client connection in a separate thread** to allow for concurrent communication.
* **Storing connected clients and their names.**
* **Broadcasting messages** from one client to all other connected clients.
* **Notifying clients when a user joins or leaves** the chat.

**Key Components:**

* `clients = {}`: A dictionary to keep track of connected clients, mapping their names to their socket objects.
* `handle_client(client_socket, client_address)`: This function is run in a new thread for each connected client. It receives messages from the client and broadcasts them.
* `broadcast_message(message)`: Sends a given message to all currently connected clients.
* `start_server()`: Initializes the server socket, binds it to a port, and starts listening for connections.

### `client.py`

The client-side application is responsible for:

* **Connecting to the server.**
* **Sending the client's chosen name** to the server.
* **Sending messages typed by the user** to the server.
* **Receiving messages from the server** and displaying them in the console.
* **Handling message input and display in separate threads** to allow for continuous sending and receiving.

**Key Components:**

* `receive_messages(client_socket)`: Listens for and displays messages received from the server.
* `send_message(client_socket)`: Takes user input and sends it to the server. It also clears the input line after sending for a cleaner UI.
* `start_client()`: Initializes the client socket, connects to the server, and starts the sending and receiving threads.

## Troubleshooting
---
* **"Connection refused" error**: Ensure the `server.py` is running before you try to connect clients. Also, make sure the `PORT` in both `server.py` and `client.py` is the same (default is 1234).
* **Messages not appearing**: Check your firewall settings to ensure that connections on port 1234 are allowed.

---

## Future Enhancements
---
* **Private Messaging**: Allow users to send direct messages to specific individuals.
* **Error Handling**: More robust error handling for network issues or unexpected client disconnections.
* **Chat Commands**: Add special commands (e.g., `/quit`, `/help`).
* **Message History**: Store and display a limited chat history.

---

## Contributing
---
Feel free to fork the repository and contribute to this project. Any improvements or new features are welcome!

---

## License
---
This project is open source and available under the MIT License.

---
