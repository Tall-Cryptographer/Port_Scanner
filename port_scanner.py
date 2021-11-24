import socket
import subprocess
import sys
from datetime import datetime
from colorama import Fore,init

# a = subprocess.call('cls')
website = input(Fore.BLUE + 'please insert your WEBSITE or IP : '+Fore.WHITE)
if website[0].isdigit:
    ip = socket.gethostbyname(website)
else:
    ip = website
for port in range(20,25):
    sock=socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    res = sock.connect_ex((ip,port))
    if res == 0:
        print(Fore.YELLOW + 'port '+ Fore.RED +str(port)+ Fore.YELLOW +' is open')
