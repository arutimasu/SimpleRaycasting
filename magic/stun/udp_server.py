import socket
 
# Создаем сокет
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
 
# Привязываем сокет к IP-адресу и порту
server_socket.bind(('localhost', 12345))
 
print("Сервер запущен на порту 12345 и ожидает входящих данных...")
 
# Получаем данные от клиента
data, client_address = server_socket.recvfrom(1024)
print(f"Получены данные от {client_address}: {data}")
 
# Закрываем сокет
server_socket.close()
