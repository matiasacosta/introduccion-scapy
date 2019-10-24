from scapy.all import ICMP, IP, sr1

# ttl = 128 -> Windows / tll = 64 -> MacOS y Linux
paquete = IP(dst="192.168.1.1")/ICMP()/"Prueba de Spoofing"
respuesta = sr1(paquete, timeout=10, verbose=False, iface="wlp3s0")

if not respuesta:
    print("No se obtuvo respuesta")
elif IP in respuesta:
    if respuesta.getlayer(IP).ttl <= 64:
        so = "Linux o MacOS"
    else:
        so = "Windows"
    print(f"El valor de ttl es {respuesta.getlayer(IP).ttl} por lo tanto el sistema operativo es {so}")