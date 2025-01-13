#!/usr/bin/env python3
# from scapy.all import *
# import socket
# import struct
# def main():
    #host="127.0.0.1"
    #s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
    #s.bind((host,0))
    #s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
    #conf.L3socket=L3RawSocket
    #data = ''
    #while True:
        #command = input('# Enter message: ')
        #создаём ICMP-пакет с командой в качестве полезной нагрузки
        #pinger = IP(dst="188.191.29.54")/ICMP(id=0x0001, seq=0x1)/command#IP(dst="127.0.0.1")/ICMP()#IP(dst="localhost")/ICMP(id=0x0001, seq=0x1)/command
        #send(pinger)
        # for i in range(2):
            # data = s.recvfrom(65535)[0]
            # ip_header = data[0:20]
            # ip_struct = struct.unpack('!BBHHHBBH4s4s' , ip_header)
            # #icmp_header = data[20:28]
            # #icmp_type, code, checksum, packet_id, sequence = struct.unpack("bbHHh", icmp_header)

            # if socket.inet_ntoa(ip_struct[9]) == host:
                # #print(data.decode('utf-8'))#.encode("utf-8"))
                # print('{} --> icmp: Type: {}, Code: {}, Data: {}'.format(socket.inet_ntoa(ip_struct[8]), *struct.unpack('BB', data[20:22]),data[28:].decode('utf-8')))
                # print(data[28:].decode('utf-8'))
            
        # ждём ICMP-сообщение с ответом от агента
        #sr1(IP(dst="127.0.0.1")/ICMP())
        
        
        
        
        #rx = sniff(count=1, timeout=0.5)
        
        #rx = sniff(filter="icmp", count=1)
        # если агент не на локальной машине, используйте это: rx = sniff(filter="icmp", count=1)
        #print(rx[0][Raw].load.decode("utf-8"))
#if __name__ == "__main__":
    #main()
import stun
import scapy.all as scapy
from scapy.all import Ether, Dot3
#scapy.send(scapy.IP()/scapy.ICMP(id=1, seq=1))
count = 0
for i in range(8):
    for j in range(3):
        integer_val = 0
        count+=1
        #scapy.send(scapy.IP(src="212.110.156.44", dst="8.8.8.8", ttl=i+1)/scapy.ICMP(id=0x0001, seq=count,length=64))
        nat_type, external_ip, external_port = stun.get_ip_info(stun_host='stun.ekiga.net')

        print(f"Тип NAT: {nat_type}")
        print(f"Внешний IP: {external_ip}")
        print(f"Внешний порт: {external_port}")
        scapy.send(scapy.IP(src="192.168.0.111", dst=external_ip, ttl=i+1)/scapy.UDP(sport=external_port, dport=external_port))
        #/Ether(dst="76:f5:38:75:95:e1"))#")#scapy.UDP(dport=55555, sport=55555)/"erthetiu")#integer_val.to_bytes(64, 'little')) #/scapy.IP(dst="192.168.0.111", src="188.191.29.54")/scapy.UDP(dport=137, sport=137))
#print(scapy.IP(dst="188.191.29.54")/scapy.ICMP(id=0x0001, seq=0x1,length=64))/"00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"))#/scapy.IP(dst="192.168.0.111", src="188.191.29.54")/scapy.UDP(dport=137,sport=137))
#76:f5:38:75:95:e1