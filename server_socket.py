import socket

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((SERVER_HOST, SERVER_PORT))

server_socket.listen(1)

print(f"[*] Listening on {SERVER_HOST}:{SERVER_PORT}")

client_socket, client_address = server_socket.accept()
print(f"[*] Accepted connection from {client_address[0]}:{client_address[1]}")

data = client_socket.recv(1024)
print(f"[*] Received data from client: {data.hex()}")

response_packet = bytes.fromhex('55AAC410006504')
client_socket.send(response_packet)
print("[*] Sent response packet to client")

client_socket.close()
server_socket.close()
