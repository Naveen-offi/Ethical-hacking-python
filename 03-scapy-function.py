from scapy.all import IP, ls

dst_ip = "1.1.1.1"

ip_layer = IP(dst=dst_ip)

print(ls(ip_layer))

print(ip_layer.src)
print(ip_layer.dst)
print(ip_layer.id)

