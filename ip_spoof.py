from scapy.all import *

send(IP(src="192.168.1.111", dst = "192.168.1.1") /ICMP()/"Prueba de Spoofing")

