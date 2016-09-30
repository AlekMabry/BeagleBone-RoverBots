import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
xboxInput = [0,0]

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    xboxInput = data.split(" ")

    print xboxInput[0]
    print xboxInput[1]



    print "received message:", data
