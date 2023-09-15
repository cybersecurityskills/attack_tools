from scapy.all import *
import sys

if len(sys.argv) < 2:
  print("Usage: packet_send_icmp.py SRC_IP DST_IP ICMP_TYPE\n")  
  sys.exit()

p1 = IP(src=sys.argv[1],dst=sys.argv[2])/ICMP(type=int(sys.argv[3]))
print("Sending",p1)
send(p1) 
