import socket

def start_tcp_server(host='0.0.0.0', port=5000):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Servidor TCP aguardando conexões em {host}:{port}...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Conexão recebida de {client_address}")
        
        message = client_socket.recv(1024).decode()
        print(f"Mensagem recebida: {message}")
        
        response = f"Olá, {client_address}! Sua mensagem foi recebida."
        client_socket.send(response.encode())
        
        client_socket.close()

if __name__ == "__main__":
    start_tcp_server()
