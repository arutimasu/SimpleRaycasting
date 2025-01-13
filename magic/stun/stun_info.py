#import upnpclient
import stun
import socket
#import miniupnpc
#import upnpy
#import threading



while True:
        nat_type, external_ip, external_port = stun.get_ip_info()
        #nat_type, external_ip, external_port = stun.get_ip_info(stun_host='stun.counterpath.net')

        print(f"Тип NAT: {nat_type}")
        print(f"Внешний IP: {external_ip}")
        print(f"Внешний порт: {external_port}")
#LPORT = 65000

#LHOST = '0.0.0.0'

# Create an instance of the UPnP library
#upnp = miniupnpc.UPnP()
#upnp = upnpy.UPnP()

# Discover UPnP/IGD devices on the network
#upnp.discoverdelay = 200
#upnp.discover()
#devices = upnp.discover()
#devices = upnpclient.discover()
#print(devices)

# Get the UPnP/IGD gateway's IP address
#gateway = upnp.selectigd()
#gateway_ip_address = upnp.lanaddr

#device = upnp.get_igd()
#d = devices[0]
#print(d)
#print(d.WANIPConn1.GetStatusInfo())

#device.get_services()

#service = device['WANPPPConnection.1']
#service.get_actions()

# Get the external IP address of the UPnP/IGD gateway
#external_ip_address = upnp.externalipaddress()

### Создаем сокет
##server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
## 
### Привязываем сокет к IP-адресу и порту
##server_socket.bind(("192.168.0.111", port))
## 
##print("Сервер запущен и ожидает входящих данных...")


# Add a port forwarding rule on the UPnP/IGD gateway
##upnp.addportmapping(
##    port,#external_port,  # external port to forward
##    'UDP',          # protocol to forward (TCP or UDP)
##    gateway_ip_address,  # local IP address to forward to
##    port,#internal_port,  # internal port to forward to
##    'UPnP Port Forwarding',  # description of the port forwarding rule
##    ''
##)
##service.AddPortMapping(
##    NewRemoteHost='',
##    NewExternalPort=port,
##    NewProtocol='UDP',
##    NewInternalPort=port,
##    NewInternalClient='192.168.0.111',
##    NewEnabled=1,
##    NewPortMappingDescription='Test port mapping entry from UPnPy.',
##    NewLeaseDuration=0
##)
##d.WANIPConn1.AddPortMapping(
##        NewRemoteHost='0.0.0.0',
##        NewExternalPort=port,
##        NewProtocol='UDP',
##        NewInternalPort=port,
##        NewInternalClient='192.168.0.111',
##        NewEnabled='1',
##        NewPortMappingDescription='Testing',
##        NewLeaseDuration=10000)
#print(f"A new UPnP rule set on {gateway_ip_address}:{port}")

# Используем полученные данные для настройки игры
#game.setup_network(external_ip, external_port)

# Создаем сокет
#server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
 
# Привязываем сокет к IP-адресу и порту
#server_socket.bind(("192.168.0.111", external_port))
 
#print("Сервер запущен и ожидает входящих данных...")

#while True:
    # Получаем данные от клиента
    #data, client_address = server_socket.recvfrom(1024)
    #print(f"Получены данные от {client_address}: {data}")
 
# Закрываем сокет
#server_socket.close()
