#!/bin/python3

import sys
import socket
from datetime import datetime

if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1])
else:
	print("Invalid Number of Arguements")
	print("Syntax: python3 portscan <ip>")

if len(sys.argv) == 2:	
	print("How many Port numbers you want to find?")
	start = int(input("Start: "))
	end = int(input("End: "))

	print("-"*50)
	print("Target: " + target)
	print("Date and Time Started: " + str(datetime.now()))
	print("-"*50)

	try:
		for port in range(start, end):
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			socket.setdefaulttimeout(1)
			result = s.connect_ex((target, port))
			if result == 0:
				print("Port number {} is open".format(port))

	except KeyboardInterrupt:
		print("Exiting the program in 3.....2.....1")
		sys.exit()
	
	except socket.gaierror:
		print("Hostname couldn't be resolved")
		print("Exiting the program in 3.....2.....1")
		sys.exit()
	
	except socket.error:
		print("Couldn't connect to the Server")
		print("Exiting the program in 3.....2.....1")
		sys.exit()
	
