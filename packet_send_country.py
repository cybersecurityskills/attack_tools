from scapy.all import *
import sys

countries = {}
countries["CHINA"] = '183.136.225.31' 
countries["CANADA"] = '159.203.46.152' 
countries["ITALY"] = '192.71.26.76'
countries["VIETNAM"] = '123.30.149.76'
countries["KOREA"] = '61.99.254.192'
countries["MOLDOVA"] = '104.28.156.58'
countries["SWEDEN"] = '185.246.130.69'
countries["US"] = '45.134.144.113'
countries["PAKISTAN"] = '101.53.233.81'



if len(sys.argv) < 2:
  print("Usage: packet_send_country.py COUNTRY DST_IP \n")  
  print("Valid countries are:"," ".join(countries.keys()))
  sys.exit()


ip = IP(src=countries[sys.argv[1]],dst=sys.argv[2])
p1 = (ip)
print("Sending",p1)
send(p1,iface="enp0s8") 
