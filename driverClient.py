import socket
import time
import xboxdrv

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
MESSAGE = ["0.0000", "0.0000"]
MESSAGE[0] = "0.0000"
MESSAGE[1] = "0.0000"

print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT
print "message:", MESSAGE

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    if ord('a') == True:
        MESSAGE[0] = "1.0000"
    else:
        MESSAGE[0] = "0.0000"

    if ord('d') == True:
        MESSAGE[1] = "1.0000"
    else:
        MESSAGE[1] = "0.0000"

    sock.sendto(MESSAGE[0]+" "+MESSAGE[1], (UDP_IP, UDP_PORT))
    time.sleep(5)
