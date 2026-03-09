import portscanner

targets_ip = input('[+] * Enter targets to scan for vulnerable ports: ')
port_number = int(input('[+] * Enter amount of ports you want to scan(500 - first 500 ports): '))
vul_file = input('[+] * Enter path to the file with vulnerable softwares: ')

portscanner.scan(targets_ip)