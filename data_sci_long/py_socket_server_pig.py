#py_socket_server_pig.py
"""Pig Latin server"""

import socket
import py_socket_pig_latin_translator as pig_speak 
#keep connectin info (maybe passwords, etc.) separate
from py_socket_connector_info import\
     ip_address, port, protocol_family_name, socket_type

#create a socket and connect: 
with socket.socket(protocol_family_name, socket_type) as soc:
	soc.bind(  (ip_address, port)   )
	soc.listen(True)
	conn_object, client_addr = soc.accept()
	print("Connected to the Pig Latin Server at {}".format(client_addr[0]))
while True:
	client_sez=conn_object.recv(64)   #an arbitrary buffer size
	if not b'stop' in client_sez:
		#using sendall() - we could use send()
		conn_object.sendall(bytes(pig_speak.pig(client_sez), 'utf-8'))
	else:	
		break
	

