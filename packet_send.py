from scapy.all import *

ip = IP(src='192.168.100.1',dst='192.168.100.2')
tcp = TCP(sport=12345,dport=22,flags='S',seq=12344)
send(ip/tcp)
