from scapy.all import IP, ICMP, sr1

src_ip = "1.1.1.5"
dst_ip = "1.1.1.1"

# Seting ip layer
ip_layer = IP(src=src_ip, dst=dst_ip)

# Setting ICMP request
icmp_req = ICMP(id=100) # id=100 is used to send data

# setting packets
packet = ip_layer / icmp_req

# Send and Receving 
respond = sr1(packet, iface="eth0")

if respond:
    print(respond.show())
