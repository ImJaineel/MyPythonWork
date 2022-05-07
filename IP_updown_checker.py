import nmap, socket

ip_addr = input('Enter ip or url to check if it is up or down: ')
scanner = nmap.PortScanner()
host = socket.gethostbyname(ip_addr)
print(scanner.scan(host, '1', '-v'))
print("IP Status: ",scanner[host].state())