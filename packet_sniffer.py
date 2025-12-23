from scapy.all import sniff

def packet_callback(packet):
    print(packet.summary())

def start_sniffer(interface):
    print(f"[+] Sniffing started on interface: {interface}")
    sniff(iface=interface, prn=packet_callback, store=False)

if __name__ == "__main__":
    interface = "eth0"   # Change to wlan0 / Wi-Fi interface if needed
    start_sniffer(interface)
