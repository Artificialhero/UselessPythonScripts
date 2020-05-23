#!/usr/bin/env
#this is a tool to automate banner grabbing in python. Give a list of ports to bannergrab.
#Sorry for spaghetti code, Its for personal uses!

import socket
import sys
import os


inpFile = input("Hello! Please insert path to a list of ports.")
inpIP = input("Please insert the target IP: ")


def readFile():
    #make array of ports
    global portArray
    with open(inpFile, "r") as f:
        portArray = f.read().splitlines()
        
    print(portArray)
    
def grabBanner(ipAddress, port):
    s=socket.socket()
    s.connect((ipAddress,port))
    banner = s.recv(1024)
    print (ipAddress + ':' + banner)
    
#def main():
    #TO DO: Iterate over each port, make it int.
    #for port in portArray:
        #ipAddress = inpIP
        #grabBanner(ipAddress,port)
        
    
readFile()
#main()
