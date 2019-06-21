from scapy.all import DNS, DNSQR, DNSRR, dnsqtypes
import socket
import threading
from random import randint


    
    
# Create a TCP/IP socket(UDP type of transmission)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Bind the socket to the port
server_address = ('192.168.43.187',1337)
sock.bind(server_address)
print("the fake dns server is up now")
while True:
  request, address = sock.recvfrom(4096)
  print("Accepting transmission from "+" "+address[0]+" "+str(address[1]))
  dns = DNS(request)
  query = dns[DNSQR].qname.decode('ascii')
  print(query)
  response = DNS(id=dns.id, ancount=1, qr=1,an=DNSRR(rrname=str(query), type='A', rdata=str(randint(10,220))+"."+str(randint(10,220))+"."+str(randint(10,220))+"."+str(randint(10,220))))
  sock.sendto(bytes(response), address)
   

   
