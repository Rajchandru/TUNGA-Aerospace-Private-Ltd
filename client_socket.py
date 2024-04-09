import socket

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((SERVER_HOST, SERVER_PORT))

packet = bytes.fromhex('55AADCC400006403')
client_socket.send(packet)
print("[*] Sent packet to server")

response = client_socket.recv(1024)
print(f"[*] Received response from server: {response.hex()}")

client_socket.close()
