#!/usr/bin/python3
import nmap
import pyfiglet

banner = pyfiglet.figlet_format("Network Scanner", justify ='centre', font='cybermedium')

scanner = nmap.PortScanner()
print(banner)
print("Welcome, this is a simple nmap automation tool")
print("<----------------------------------------------------->")

ipv4_address = input("Please enter the IP address you want to scan: ")
print("The IP you entered is: ", ipv4_address)
type(ipv4_address)

resp = input("""\nPlease enter the scan you want to run
                1)SYN ACK Scan (TCP)
                2)UDP Scan
                3)Comprehensive Scan \n""")
                
print("You have selected option: ", resp)

resp_dict={'1':['-v -sS','tcp'],'2':['-v -sU','udp'],'3':['-v -sS -sV -sC -A -O','tcp']}

if resp not in resp_dict.keys():

    print("enter a valid option")
    
else:
    print("nmap version: ", scanner.nmap_version())
    
    scanner.scan(ipv4_address,"1-1024",resp_dict[resp][0]) #the port range to scan, the last part is the scan type
    
    print(scanner.scaninfo())
    
    if scanner.scaninfo()=='up':
        print("Scanner Status: ",scanner[ipv4_address].state())
        print(scanner[ipv4_address].all_protocols())
        print("Open Ports: ",scanner[ipv4_address][resp_dict[resp][1]].keys())  #display all open ports
