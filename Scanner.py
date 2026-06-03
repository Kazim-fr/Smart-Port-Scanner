import socket
import time
import threading
from urllib.parse import urlparse
from concurrent.futures import ThreadPoolExecutor

# Thread-safe lock
lock = threading.Lock()

# Store open ports
open_ports = []


def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)

        result = sock.connect_ex((ip, port))

        if result == 0:

            try:
                service = socket.getservbyport(port)
            except:
                service = "Unknown"

            with lock:
                open_ports.append((port, service))
                print(f"{port:<10} OPEN      {service}")

        sock.close()

    except:
        pass


def main():

    target = input("Enter target website or IP: ").strip()

    # Handle URLs
    if target.startswith("http://") or target.startswith("https://"):
        target = urlparse(target).netloc

    try:
        ip = socket.gethostbyname(target)

    except socket.gaierror:
        print("\n[ERROR] Invalid hostname or unable to resolve domain.")
        return

    print("\n" + "=" * 50)
    print("SMART PORT SCANNER")
    print("=" * 50)

    print(f"Target : {target}")
    print(f"IP      : {ip}")

    print("\nScanning ports 1-1024...\n")

    print("-" * 40)
    print("PORT      STATUS    SERVICE")
    print("-" * 40)

    start_time = time.time()

    # Multithreaded scanning
    with ThreadPoolExecutor(max_workers=100) as executor:
        for port in range(1, 1025):
            executor.submit(scan_port, ip, port)

    end_time = time.time()

    # Sort ports before displaying summary
    open_ports.sort(key=lambda x: x[0])

    print("\n" + "=" * 50)
    print("SCAN SUMMARY")
    print("=" * 50)

    print(f"Target           : {target}")
    print(f"IP Address       : {ip}")
    print(f"Open Ports Found : {len(open_ports)}")
    print(f"Scan Time        : {end_time - start_time:.2f} seconds")

    print("=" * 50)


if __name__ == "__main__":
    main()