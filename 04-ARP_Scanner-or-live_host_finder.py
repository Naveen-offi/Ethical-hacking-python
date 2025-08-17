from scapy.all import Ether, ARP, srp

boardcast = "ff:ff:ff:ff:ff:ff"
ip_range = "1.1.1.1/24"

ether_layer = Ether(dst=boardcast)
arp_layer = ARP(pdst=ip_range)

packet = ether_layer / arp_layer

answered, unanswered = srp(packet, iface="eth0", timeout=2)

for snd, rcv in answered:
    ip = rcv[ARP].psrc
    mac = rcv[Ether].src
    print(f"ip : {ip} | mac : {mac}")
