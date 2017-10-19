"""Simple socket server"""

import socket

#a little connection info:
ip_address=             'localhost'           #serving locally only
port =                  8000                  #an arbitrary 4-digit port
protocol_family_name=   socket.AF_INET        #olde type IPv4 protocol
socket_type=            socket.SOCK_STREAM    #a simple stream

#create a socket: 
with socket.socket(protocol_family_name, socket_type) as soc:

	#give it an address 
	soc.bind(  (ip_address, port)   )
	
	#ask the socket to listen for traffic
	soc.listen(True)
	conn_object, client_addr = soc.accept()
	
	#that's it!  any client can now send data to the socket
	print("Yea!  Got a connection from {}".format(client_addr[0]))
	while True:
		client_sez=conn_object.recv(32)   #an arbitrary buffer size
		if not b'stop' in client_sez:
			print(client_sez)
		else:	
			break
	

