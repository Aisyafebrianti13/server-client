import socket

# Inisialisasi socket klien
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_host = 'localhost'  # Host server
server_port = 12345  # Port server

# Mencoba terhubung ke server
client_socket.connect((server_host, server_port))

# Kirim permintaan ke server
request_data = "Ini adalah permintaan dari klien."
client_socket.send(request_data.encode('utf-8'))

# Terima respons dari server
response_data = client_socket.recv(1024).decode('utf-8')
print(f"Respons dari server: {response_data}")

# Tutup koneksi dengan server
client_socket.close()
