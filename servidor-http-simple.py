#!/usr/bin/python
# -*- coding: utf-8 -*-
# Sistemas Teleco. Sara Suárez.

import socket

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.bind(('localhost', 1234))

mySocket.listen(5)

while True:
    print 'Waiting for connections'
    (recvSocket, address) = mySocket.accept()
    print 'HTTP request received:'
    print recvSocket.recv(1024)
    recvSocket.send("HTTP/1.1 200 OK\r\n\r\n" + 
		"<html><body><h1>Hola! Eres de esta IP (" + str(address[0]) + ") y de este puerto (" + 
		str(address[1]) + ")</h1></body></html>" + "\r\n" + "<html><h1>")
recvSocket.close()
