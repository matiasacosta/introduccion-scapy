from scapy.all import *

dst_ip = "200.16.134.134"
src_port = RandShort()
dst_port=80

tcp_connect_scan_resp = sr1(IP(dst=dst_ip)/TCP(sport=src_port,dport=dst_port,flags="S"),timeout=10)
if(tcp_connect_scan_resp is None):
    print("Puerto Cerrado")
elif(tcp_connect_scan_resp.haslayer(TCP)):
    if(tcp_connect_scan_resp.getlayer(TCP).flags == 0x12):
        send_rst = sr(IP(dst=dst_ip)/TCP(sport=src_port,dport=dst_port,flags="AR"),timeout=10)
        print("Puerto Abierto")
    elif (tcp_connect_scan_resp.getlayer(TCP).flags == 0x14):
        print("Puerto Cerrado")