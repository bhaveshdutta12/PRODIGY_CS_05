# PRODIGY_CS_05
# Network Packet Analyzer

This Python-based packet sniffer tool captures and analyzes network packets. It displays key information such as source and destination IP addresses, protocols, and payload data. The tool is built using the `scapy` library for educational and ethical purposes.

## Features

- **Packet Capturing**: Captures packets on a specified network interface.
- **Protocol Analysis**: Supports TCP, UDP, and ICMP protocols.
- **Real-time Packet Inspection**: Displays source and destination IP addresses, protocol, and payload data.
  
## Prerequisites

- Python 3.x
- `scapy` library

To install `scapy`, run:

```bash
pip install scapy
```
# Usage
1. Clone the repository or download the script.

2. Modify the network interface in the script to your actual network interface. For example:
```bash
interface = "wlan0"  # Replace with your actual network interface name
```
3. Run the script with root/administrator privileges:
```bash
sudo python3 packet_sniffer.py
```
4. The tool will start capturing packets and printing relevant information to the console.
