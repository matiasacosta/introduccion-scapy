from scapy.all import *

sniff(iface= "wlp3s0", prn= lambda x : x. summary)