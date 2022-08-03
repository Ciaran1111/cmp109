from socket import *
serverPort = 12000
serverSocket = socket (AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print("Sever is running")

# main loop
while 1:
    # listen out for data from client
    operation, clientAddress = serverSocket.recvfrom (2048)
    n1, clientAddress = serverSocket.recvfrom (2048)
    n2, clientAddress = serverSocket.recvfrom (2048)

    total = 0

    # working out what operation is to be used
    if operation.decode() == '+':
        total = int(n1) + int(n2)
    elif operation.decode() == '-':
        total = int(n1) - int(n2)
    elif operation.decode() == 'x':
        total = int(n1) * int(n2)
    elif operation.decode() == '/':
        total = int(n1) / int(n2)


    # casting total to string then sending it over using UTF-8 encoding
    total = str(total)
    serverSocket.sendto(total.encode('utf-8'), clientAddress)
