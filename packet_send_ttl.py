from scapy.all import *
import sys

if len(sys.argv) < 2:
  print("Usage: packet_send_ttl.py SRC_IP DST_IP TTL_VALUE\n")  
  sys.exit()

ip = IP(src=sys.argv[1],dst=sys.argv[2],ttl=int(sys.argv[3]))
p1 = (ip)
print("Sending",p1,"TTL",p1.ttl)
send(p1) 
