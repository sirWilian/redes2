import socket
import os
import time

def start_tcp_client(server_host, server_port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_host, server_port))
    
    file_path = input("Digite o caminho do arquivo para enviar ao servidor: ")
    if not os.path.exists(file_path):
        print(f"[ERRO] Arquivo {file_path} não foi encontrado!")
        client_socket.close()
        return
    
    # Enviar nome do arquivo
    file_name = os.path.basename(file_path)
    client_socket.send(file_name.encode())
    file_size = os.path.getsize(file_path) # esse tamanho sera usado para comparacao
    print(f"[INFO] Iniciando envio do arquivo: {file_path}")
    print(f"[INFO] Tamanho total do arquivo: {file_size} bytes")
    
    # Confirmar prontidão do servidor
    server_ready = client_socket.recv(1024).decode()
    if server_ready != "READY":
        print("[ERRO] o servidor não está pronto para receber o arquivo.")
        client_socket.close()
        return
    
    print("[INFO] o servidor está pronto para receber o arquivo.")

    pacotes_enviados = 0
    bytes_enviados = 0
    start_time = time.time()
    # Enviar o conteúdo do arquivo
    with open(file_path, "rb") as file:
        while chunk := file.read(1024):
            client_socket.send(chunk)
            pacotes_enviados += 1
            bytes_enviados += len(chunk)
            print(f"[ENVIADO] pacote {pacotes_enviados}: {len(chunk)} bytes | Total enviado: {bytes_enviados} bytes")
            
    # Fechar a transmissão de dados (importante!)
    client_socket.shutdown(socket.SHUT_WR)
    print(f"[INFO] conexao encerrada!")
    # Recebe o end_time do servidor
    server_time = client_socket.recv(1024).decode()
    client_socket.close()
    
    end_time = float(server_time)
    total_time = end_time - start_time
    print(f"[ESTATISTICA] Arquivo {file_name} de tamanho {file_size} bytes foi enviado com sucesso.")
    print(f"[ESTATISTICA] Pacotes enviados: {pacotes_enviados}")
    print(f"[ESTATISTICA] Tempo total da transferência: {total_time:.6f} segundos")

if __name__ == "__main__":
    start_tcp_client('192.168.1.2', 5000)
