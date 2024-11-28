import socket

def start_tcp_client(server_host, server_port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_host, server_port))
    
    message = input("Digite a mensagem para enviar ao servidor: ")
    client_socket.send(message.encode())
    
    response = client_socket.recv(1024).decode()
    print(f"Resposta do servidor: {response}")
    
    client_socket.close()

if __name__ == "__main__":
    start_tcp_client('192.168.1.2', 5000)  # Substitua pelo IP do servidor
