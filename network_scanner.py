from scapy.all import ARP, Ether, srp

def scan_network(target_ip):
    print(f"[+] Scanning network: {target_ip}")
    
    arp_request = ARP(pdst=target_ip)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = broadcast / arp_request

    result = srp(packet, timeout=2, verbose=False)[0]

    devices = []
    for sent, received in result:
        devices.append({
            "ip": received.psrc,
            "mac": received.hwsrc
        })

    return devices

if __name__ == "__main__":
    devices = scan_network("192.168.1.0/24")
    print("\nDiscovered Devices:")
    for device in devices:
        print(f"IP: {device['ip']}  |  MAC: {device['mac']}")
