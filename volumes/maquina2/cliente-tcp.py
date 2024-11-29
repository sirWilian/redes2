import socket
import os
import time

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
    start_time = time.time()
    # Enviar o conteúdo do arquivo
    with open(file_path, "rb") as file:
        while chunk := file.read(1024):
            client_socket.send(chunk)
            pacotes_enviados += 1
            
    # Fechar a transmissão de dados (importante!)
    client_socket.shutdown(socket.SHUT_WR)
    
    # Recebe o end_time do servidor
    server_time = client_socket.recv(1024).decode()
    client_socket.close()
    
    end_time = float(server_time)
    total_time = end_time - start_time
    print("Arquivo enviado com sucesso.")
    print(f"Pacotes enviados: {pacotes_enviados}")
    print(f"Tempo total da transferência: {total_time:.6f} segundos")

if __name__ == "__main__":
    start_tcp_client('192.168.1.2', 5000)
