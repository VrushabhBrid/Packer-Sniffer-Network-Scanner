import socket

def scan_ports(target_ip, ports):
    print(f"[+] Scanning ports on {target_ip}")
    open_ports = []

    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        
        if sock.connect_ex((target_ip, port)) == 0:
            open_ports.append(port)
        
        sock.close()

    return open_ports

if __name__ == "__main__":
    target = "192.168.1.5"  # Change target IP
    ports = [21, 22, 23, 80, 443, 445]

    open_ports = scan_ports(target, ports)
    print("Open Ports:", open_ports)
