#!/usr/bin/env python
import socket
import sys
from datetime import datetime
import urllib.request

# Ask for input
external_ip = urllib.request.urlopen('https://api.ipify.org').read().decode('utf8')

# Print a nice banner with information on which host we are about to scan
print("-" * 60)
print("Please wait, scanning external ip address", external_ip)
print("-" * 60)

# Check what time the scan started
t1 = datetime.now()

# Using the range function to specify ports (here it will scans 22555 to 22556)

# We also put in some error handling for catching errors

try:
    for port in range(22555, 22556):  
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((external_ip, port))
        if result == 0:
            print("Port {}: 	 Open".format(port))
        sock.close()

except KeyboardInterrupt:
    print("You pressed Ctrl+C")
    sys.exit()

except socket.gaierror:
    print('Hostname could not be resolved. Exiting')
    sys.exit()

except socket.error:
    print("Couldn't connect to host")
    sys.exit()

# Checking the time again
t2 = datetime.now()

# Calculates the difference of time, to see how long it took to run the script
total =  t2 - t1

# Printing the information to screen
print('Scanning Completed in: ', total)