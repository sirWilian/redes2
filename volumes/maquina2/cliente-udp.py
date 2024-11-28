import socket

def start_udp_client(server_host, server_port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    message = input("Digite a mensagem para enviar ao servidor: ")
    client_socket.sendto(message.encode(), (server_host, server_port))
    
    response, _ = client_socket.recvfrom(1024)
    print(f"Resposta do servidor: {response.decode()}")
    
    client_socket.close()

if __name__ == "__main__":
    start_udp_client('192.168.1.2', 5001)  # Substitua pelo IP do servidor
