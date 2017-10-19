#py_socket_client_pig.py

import socket

from py_socket_connector_info import\
     ip_address, port, protocol_family_name, socket_type

#create a socket:
with socket.socket(protocol_family_name, socket_type) as soc:
    soc.connect( (ip_address, port) )
    print("Yea!  We're talking to {}\n".format(ip_address))
    while True:
        msg=input("Pig Latin translator (or 'stop'):  ")
        soc.send(bytes(msg, 'utf=8'))
        print(soc.recv(64))
        if 'stop' in msg:
            break
