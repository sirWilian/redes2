import socket
import os

def start_udp_client(server_host, server_port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Selecionar arquivo para envio
    file_path = input("Digite o caminho do arquivo para enviar ao servidor: ")
    if not os.path.exists(file_path):
        print("Arquivo não encontrado!")
        client_socket.close()
        return
    
    file_name = os.path.basename(file_path)
    client_socket.sendto(file_name.encode(), (server_host, server_port))
    print(f"Enviando arquivo: {file_name}")

    pacotes_enviados = 0
    with open(file_path, "rb") as file:
        while chunk := file.read(1024):
            client_socket.sendto(chunk, (server_host, server_port))
            pacotes_enviados += 1
    
    # Enviar indicador de fim de transmissão
    client_socket.sendto("EOF".encode(), (server_host, server_port))
    pacotes_enviados += 1
    print("Arquivo enviado com sucesso.")
    print(f"Pacotes enviados: {pacotes_enviados}")  

    # Receber confirmação do servidor
    response, _ = client_socket.recvfrom(1024)
    print(f"Resposta do servidor: {response.decode()}")

    client_socket.close()

if __name__ == "__main__":
    start_udp_client('192.168.1.2', 5001)  # Substitua pelo IP do servidor
