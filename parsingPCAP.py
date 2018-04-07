import socket
import dpkt
import time

def convertPacketsToFlows(input):

    from itertools import groupby
    from operator import itemgetter
    grouper = itemgetter('sourceIP:port', 'dstIP:dstport')
    firstResult = []
    NewList = []
    for (key, grp) in groupby(sorted(input, key=grouper), grouper):
        temp_dict = dict(zip(['sourceIP:port', 'dstIP:dstport'], key))
        if any((d['sourceIP:port'] == temp_dict['sourceIP:port'] and d['dstIP:dstport'] == temp_dict[
            'dstIP:dstport']) or (
                d['sourceIP:port'] == temp_dict['dstIP:dstport'] and d['dstIP:dstport'] == temp_dict['sourceIP:port'])
               for d in firstResult):
            continue
        temp_list = [item['id'] for item in grp]
        temp_dict['packet-count'] = len(temp_list)
        innerGrouper = itemgetter('sourceIP:port', 'dstIP:dstport')
        secondResult = []
        for (innerKey, innerGrp) in groupby(sorted(input, key=innerGrouper), innerGrouper):
            inner_temp_dict = dict(zip(['sourceIP:port', 'dstIP:dstport'], innerKey))
            if inner_temp_dict['dstIP:dstport'] == temp_dict['sourceIP:port']:
                inner_temp_list = [item['id'] for item in innerGrp]
                temp_dict['packet-count'] += len(inner_temp_list)
        firstResult.append(temp_dict)


        val = int(temp_dict['packet-count'])

        if val > 60 :
            data = [d for d in input if d['sourceIP:port'] == temp_dict['sourceIP:port'] and d['dstIP:dstport'] == temp_dict['dstIP:dstport']]
            print 'packet count= ' + str(temp_dict['packet-count'])+'   ' + str(data[0])
            NewList.append(data[0].values()[3])
    p = NewList[0]
    print "The first paket in the first grouped flow:", [d for d in myList if d['id'] == p]


f = open('/home/rashad/Downloads/slowdownload.pcap','r')
pcap = dpkt.pcap.Reader(f)

pktCounter = 0
myList = []

for ts,buff in pcap:

    pktCounter += 1

    try:
        ether = dpkt.ethernet.Ethernet(buff)

        # Packet
        ip = ether.data
        tcp = ip.data
        packetData = ip.data.data.encode("hex")
        src = socket.inet_ntoa(ip.src)
        srcport = tcp.sport
        dst = socket.inet_ntoa(ip.dst)
        dstport = tcp.dport

        # Definition of Time
        #showTime = time.gmtime(ts)
        #timeF = time.strftime("%Y/%m/%d %H:%M:%S", showTime)

        # Packet Size
        sizeP = len(buff)

        myList.append(
            {'id': pktCounter, 'packet-length': sizeP, 'sourceIP:port': str(src+':'+str(srcport)), 'dstIP:dstport': str(dst+':'+str(dstport)), 'firstPacketData': packetData})


    except AttributeError:
        pass

print "----------------------------"
convertPacketsToFlows(myList)
