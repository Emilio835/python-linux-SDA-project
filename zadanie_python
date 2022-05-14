# # MOJE IP
import os
ip_cmd = os.popen('hostname -I').read()
ip = ip_cmd.split(" ")[0]
print(ip) # 192.168.56.101
ip_prefix = ".".join(ip.split(".")[:3])+"."
print(ip_prefix)
# MASKA PODSIECI
import os
def mask_search():
    device = input("Z jakiego interfejsu sieciowego korzystasz? [np. eth0]: ")
    mask = str(os.popen(f"nmcli dev show {device} | grep  IP4.ADDRESS").read()).strip().split("/")[1]
    print(mask)
    return mask
# AKTYWNE HOSTY
from scapy.all import *
from scapy.layers.inet import *
maska = int(mask_search())
live_hosts = []
if maska == 24:
    low_limit=1
    high_limit=254
else:
    pass
for ip in range(198, 201): # ZEBY BYLO SZYBCIEJ
    adres =  ip_prefix + str(ip)
    packet = IP(dst=adres, ttl=20)/ICMP()
    reply = sr1(packet, timeout=2)
    if reply:
         print(adres, "is online")
         live_hosts.append(adres)
    else:
        print(adres, "DOWN")
otwarte_porty = []
for host in live_hosts:
    for port in range(1, 100):
        pakiet = IP(dst=host)/TCP(dport=port, sport=random.randint(20000, 50000), flags="S")
        response = sr1(pakiet)
        if str(response.getlayer(TCP).flags) == "SA":
            otwarte_porty.append(port)
    print(host, otwarte_porty)
import socket
for host in live_hosts:
    for port in otwarte_porty:
        mySocket = socket.socket()
        mySocket.connect((host, port))
        if port == 80:
            mySocket.send ("Get banner \r \n".encode())
        serverRecv = mySocket.recv((2048)).decode()
        print(serverRecv)
