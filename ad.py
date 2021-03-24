from scapy.all import *
from datetime import datetime
import binascii
import os
#(filter=....) need tcpdump installed 
#.filter(lambda p: "TCP" in p) is 
conf.use_pcap = True

def ScannerDetect(filename):
    
    #tcp packages
    pkts = rdpcap(filename).filter(lambda p: "TCP" in p)
    ipSR = dict() #ip:[#SYN,#SYNACK]
    
    for pkt in pkts:
        
        if(pkt["IP"].src not in ipSR):
                        ipSR[pkt["IP"].src] = [0,0]        
        #SYN -- send
        if(pkt["TCP"].flags == "S"):
            ipSR[pkt["IP"].src][0] += 1
        
        #SYNACK -- receive
        if(pkt["TCP"].flags == "SA"):
            ipSR[pkt["IP"].dst][1] += 1
    
    #print("Find: ")       
    for ip in ipSR:
        
        Nosyn = ipSR[ip][0]
        Nosynack = 3*ipSR[ip][1]
        if(Nosyn > Nosynack or (ipSR[ip][0] == 0 and ipSR[ip][1] == 0)):
            print(ip)
        
                
    
filename = "dns-ethereal-trace-1"#"proj3.pcap"
st = datetime.now()
ScannerDetect(filename)
et = datetime.now()
tt = et - st
print("cost: {}".format(tt))
#pkts = rdpcap(filename).filter(lambda p: "TCP" in p) #read all
#print(len(a))
#for i in range(len(pkts)):
    #print(i)
    #if("TCP" in pkts[i]):
        #pkts[i].show()
        #break
#print(len(pkts))
# if TCP,IP,Ethernet in pkt
# src: [IP].src
# det: [IP].dst
# type: [IP].proto == tcp
# flags: [TCP].flags
