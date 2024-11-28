import socket

def start_udp_server(host='0.0.0.0', port=5001):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))
    print(f"Servidor UDP aguardando mensagens em {host}:{port}...")

    while True:
        message, client_address = server_socket.recvfrom(1024)
        print(f"Mensagem recebida de {client_address}: {message.decode()}")
        
        response = f"Olá, {client_address}! Sua mensagem foi recebida."
        server_socket.sendto(response.encode(), client_address)

if __name__ == "__main__":
    start_udp_server()
