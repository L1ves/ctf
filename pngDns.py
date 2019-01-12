from scapy.all import *

r = rdpcap("dnscap.pcap")

a = ""

b = ""
c = ""
new = ""

f = open("flag.png","w")

for i in range (0,len(r)):
	if r[i].haslayer(DNSQR) and not r[i].haslayer(DNSRR):
		a = r[i][DNSQR].qname
		b = a.replace(".skullseclabs.org.","")
		b = b.replace(".","").decode("hex")[9:]

		if b == c:
			continue

		c = b

		if 6 < i <365:
			new = new + b

f.write(new)

f.close()
