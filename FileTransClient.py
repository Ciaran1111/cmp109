from socket import *
# server IP and Port variables
Server_IP = '127.0.0.1'
sPort = 12000
# creating instance of socket object
client = socket(AF_INET, SOCK_STREAM)
# connecting to the server using port and IP
client.connect((Server_IP, sPort))
print('Connected to server')

filename = "test.txt"
# opens the file
file = open(filename, "r")

# reading the data from the file then sending the encoded version to server
fileData = file.read()
client.send(fileData.encode())

file.close()

# take in response from server
no_words = client.recv(1024)
no_chars = client.recv(1024)

# outputs the number of words and characters
print("number of words", no_words.decode(), "number of characters:", no_chars.decode())


client.close()

