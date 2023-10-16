import socket

# Inisialisasi socket server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_host = 'localhost'  # Host yang akan digunakan
server_port = 12345  # Port yang akan digunakan

# Binding socket ke alamat dan port yang ditentukan
server_socket.bind((server_host, server_port))

# Mendengarkan hingga ada koneksi masuk
server_socket.listen(5)

print(f"Server mendengarkan di {server_host}:{server_port}")

while True:
    # Menerima koneksi dari klien
    client_socket, client_address = server_socket.accept()

    print(f"Menerima koneksi dari {client_address}")

    # Menerima data dari klien
    request_data = client_socket.recv(1024).decode('utf-8')
    print(f"Permintaan dari klien: {request_data}")

    # Proses permintaan dari klien (di sini kita hanya memberikan respons sederhana)
    response_data = "Ini adalah respons dari server."
    client_socket.send(response_data.encode('utf-8'))

    # Tutup koneksi dengan klien
    client_socket.close()
