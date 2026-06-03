\# Smart Port Scanner



A multi-threaded TCP Port Scanner built in Python.



\## Features



\- Scan ports 1-1024

\- Multi-threaded scanning

\- Detect open ports

\- Identify common services

\- URL and hostname support

\- DNS resolution

\- Scan statistics



\## Technologies Used



\- Python

\- Socket Programming

\- ThreadPoolExecutor

\- Networking Fundamentals



\## How It Works



The scanner attempts to establish TCP connections with target ports.



If a connection is successful, the port is considered open.



The application then identifies the associated service and displays the results.



\## Example Output



```text

Target : scanme.nmap.org

IP     : 45.33.xxx.xxx



PORT      STATUS    SERVICE



22        OPEN      ssh

80        OPEN      http

443       OPEN      https




## Screenshot

![Scanner Demo](screenshots/scan-demo.png)



\## Author



Kazim Sheikh

