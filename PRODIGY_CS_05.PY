from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP, ICMP

# Function to process and analyze packets
def packet_callback(packet):
    if IP in packet:
        ip_layer = packet[IP]
        protocol = None
        payload = None

        if TCP in packet:
            protocol = "TCP"
            payload = packet[TCP].payload
        elif UDP in packet:
            protocol = "UDP"
            payload = packet[UDP].payload
        elif ICMP in packet:
            protocol = "ICMP"
            payload = packet[ICMP].payload

        # Display packet details
        print(f"[+] Packet: {ip_layer.src} -> {ip_layer.dst} | Protocol: {protocol}")
        print(f"Payload: {payload}")
        print("-" * 60)

# Start sniffing network packets
def start_sniffer(interface):
    print(f"[*] Starting packet sniffer on {interface}")
    sniff(iface=interface, prn=packet_callback, store=False)

# Example usage
if __name__ == "__main__":
    interface = "eth0"  # Replace with your network interface
    start_sniffer(interface)
