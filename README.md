# Smart Port Scanner 

A multi-threaded TCP Port Scanner built using Python that scans a target host for open ports and identifies common services running on those ports.

## Features

* Multi-threaded port scanning for improved performance
* Scans TCP ports from 1 to 1024
* Detects open ports
* Identifies common services (HTTP, HTTPS, SSH, etc.)
* Supports IP addresses, domain names, and URLs
* DNS hostname resolution
* Displays scan statistics and execution time
* Error handling for invalid targets

## Technologies Used

* Python 3
* Socket Programming
* ThreadPoolExecutor
* Networking Fundamentals
* Multithreading

## Project Structure

```text
Smart-Port-Scanner/
│
├── scanner.py
├── README.md
├── requirements.txt
├── .gitignore
│
└── screenshots/
    └── scan-demo.png
```

## How It Works

1. Accepts a target hostname, URL, or IP address.
2. Resolves the hostname to an IP address.
3. Creates multiple worker threads.
4. Attempts TCP connections to ports 1-1024.
5. Identifies open ports and associated services.
6. Displays scan results and execution time.

## Example Usage

```bash
python scanner.py
```

Input:

```text
Enter target website or IP: scanme.nmap.org
```

Output:

```text
==================================================
SMART PORT SCANNER
==================================================
Target : scanme.nmap.org
IP      : 45.33.xxx.xxx

PORT      STATUS    SERVICE
----------------------------------------
22        OPEN      ssh
80        OPEN      http
443       OPEN      https

==================================================
SCAN SUMMARY
==================================================
Open Ports Found : 3
Scan Time        : 2.14 seconds
==================================================
```


## Disclaimer

This tool is intended for educational purposes and authorized security testing only. Always obtain proper permission before scanning systems you do not own or manage.

## Author

**Kazim Sheikh**
