from socket import *

serverIP = '127.0.0.1'
sPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((serverIP, sPort))


serverSocket.listen(1)

print('Server is running')

while 1:
    connectionSocket, port = serverSocket.accept()
    print ('Client has succesfully connected')
    # listening out for the data from  the client in this case, filedata then decoding that data
    filedata= connectionSocket.recv(1024)
    # changing the file data to a string 
    filedata = str(filedata.decode())
        
    #works out num of chars
    no_chars = len(filedata) 
    #works out num of words
    no_words = len(filedata.split()) 
    # converting to str from byte
    no_chars = str(no_chars)
    no_words = str(no_words)


    #send no_words, no_chars to client using sendall 
    connectionSocket.sendall(no_words.encode())
    connectionSocket.sendall(no_chars.encode())

    print('Data has been sent over to client ')

# close TCP connection
connectionSocket.close()
