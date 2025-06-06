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
