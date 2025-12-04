import socket

# Port Scanner
target_ip = input("Enter Target IP Address: ")
portrange = input("Enter Port Range (e.g., 20-80): ")

low_port = int(portrange.split('-')[0]) # Get the lower bound of the port range
high_port = int(portrange.split('-')[1]) # Get the upper bound of the port range

print(f"Scanning ports {low_port} to {high_port} on {target_ip}...")

for port in range(low_port, high_port + 1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    status = s.connect_ex((target_ip, port))
    if status == 0:
        print(f"Port {port} is open")
    else:
        print(f"Port {port} is closed")
    s.close()
