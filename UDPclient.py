from socket import *
serverIP = "localhost"
serverPort = 12000
clientSocket = socket (AF_INET, SOCK_DGRAM)


# take inputs from user
operation = input("What kind of operation would you like to perform ( + x / -)")
No1 = input("Enter the first number")
No2 = input("Enter the second number")

# encode and send them to the server
clientSocket.sendto(operation.encode(), (serverIP, serverPort))
clientSocket.sendto(No1.encode(), (serverIP, serverPort))
clientSocket.sendto(No2.encode(), (serverIP, serverPort))

# take in asnwer from the server
answer = clientSocket.recv(2048)

# decode and print answer
print(answer.decode())
clientSocket.close()


