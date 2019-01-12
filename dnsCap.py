from scapy.all import *

r = rdpcap("dnscap.pcap")

a = ""

b = ""

for i in range (0, len(r)):
    a = r[i][DNSQR].qname
    b = a.replace(".skullseclabs.org.","")
    print(b.replace(".","")).decode("hex")
