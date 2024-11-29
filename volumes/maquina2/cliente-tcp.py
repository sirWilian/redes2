import socket
import os

def start_tcp_client(server_host, server_port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_host, server_port))
    
    file_path = input("Digite o caminho do arquivo para enviar ao servidor: ")
    if not os.path.exists(file_path):
        print("Arquivo não encontrado!")
        client_socket.close()
        return
    
    # Enviar nome do arquivo
    file_name = os.path.basename(file_path)
    client_socket.send(file_name.encode())
    
    # Confirmar prontidão do servidor
    server_ready = client_socket.recv(1024).decode()
    if server_ready != "READY":
        print("Erro: o servidor não está pronto para receber o arquivo.")
        client_socket.close()
        return
    
    pacotes_enviados = 0
    # Enviar o conteúdo do arquivo
    with open(file_path, "rb") as file:
        while chunk := file.read(1024):
            client_socket.send(chunk)
            pacotes_enviados += 1
    
    print("Arquivo enviado com sucesso.")
    print(f"Pacotes enviados: {pacotes_enviados}")
    client_socket.close()

if __name__ == "__main__":
    start_tcp_client('192.168.1.2', 5000)  # Substitua pelo IP do servidor
