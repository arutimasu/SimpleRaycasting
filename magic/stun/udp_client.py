import socket

#ip = input('Enter the IP address: ') 
#port = input('Enter the port: ') 
# Создаем сокет
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for i in range(8):
    # Отправляем данные серверу
    print("Sending packet #", i)
    client_socket.sendto(b'Hello, server!', ("188.191.29.54", 1530))
 
# Закрываем сокет
client_socket.close()
