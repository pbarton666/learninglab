"""Simple socket server.  
   See https://stackoverflow.com/questions/16772465/ for 2.x
     context manager compatibility"""

import socket

#we need a bit of info first:
ip_address=             'localhost'
port =                  8000
protocol_family_name=   socket.AF_INET
socket_type=            socket.SOCK_STREAM

#create a socket and connect to the address the server is listening to: 
with socket.socket(protocol_family_name, socket_type) as soc:
    soc.connect( (ip_address, port) )
    
    #that's it!  we can talk to the server.
    print("Yea!  We're talking to {}\n".format(ip_address))
    while True:
        msg=input("Talk to the server (or 'stop'):  ")
        soc.send(bytes(msg, 'utf=8'))
        if 'stop' in msg:
            break
