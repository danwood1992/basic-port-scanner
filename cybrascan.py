import nmap

nm = nmap.PortScanner()

print("cybrascan  v1.0 ")
print("<----------------------------------------------------->")

ipv4 = input("Enter IPv4 address : ")
print("IP you entered is: ", ipv4)
type(ipv4)

resp = input("""\nScan you want to run
                1)SYN ACK Scan
                2)UDP Scan
                3)Comprehensive Scan \n""")
print("You have selected option: ", resp)
resp_dict={'1':['-v -sS','tcp'],'2':['-v -sU','udp'],'3':['-v -sS -sV -sC -A -O','tcp']}
if resp not in resp_dict.keys():
    print("enter a valid option")
else:
    print("nmap version: ", nm.nmap.version())
    nm.scan(ipv4,"1-1024",resp_dict[resp][0]) #the # are port range to scan, the last part is the scan type
    print(nm.scaninfo())
    if nm.scaninfo()=='up':
        print("Scanner Status: ", nm[ipv4].state())
        print(nm[ipv4].all_protocols())
        print("Open Ports: ",nm[ipv4][resp_dict[resp][1]].keys())  #display all open ports