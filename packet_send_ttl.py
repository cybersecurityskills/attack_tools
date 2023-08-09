from scapy.all import *

ip = IP(src='10.0.1.1',dst='10.0.1.2',ttl=5)
p1 = (ip)
print("Sending",p1)
send(p1) 
