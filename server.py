import socket
import datetime

host = '127.0.0.1'
port = 1234
server_address = (host, port)

s_socket = socket.socket()
s_socket.bind(server_address)

s_socket.listen(1)
while True:
    if datetime.datetime.now().hour == 0: #Exit if time is. 00:00
        break
    print('Server is running and waiting for connection...')

    #Connect new user
    connection, addr = s_socket.accept()
    print('Connection address:', addr)

    #Recive data
    while True:
        data = connection.recv(1024)
        if data:
            print(str(datetime.datetime.now()) + ' Received data:', data)
            connection.sendall(data)
        else:
            break
s_socket.close()
