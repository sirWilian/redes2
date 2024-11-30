import socket
import os
import time

def start_udp_client(server_host, server_port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        file_path = input("Digite o caminho do arquivo para enviar ao servidor (ou 'exit' para encerrar): ").strip()
        
        if file_path.lower() == 'exit':
            client_socket.sendto("exit".encode(), (server_host, server_port))
            print("[INFO] Enviando comando de encerramento ao servidor.")
            break

        if not os.path.exists(file_path):
            print(f"[ERRO] Arquivo {file_path} não foi encontrado!")
            continue

        file_name = os.path.basename(file_path)
        client_socket.sendto(file_name.encode(), (server_host, server_port))
        file_size = os.path.getsize(file_path)
        print(f"[INFO] Iniciando envio do arquivo: {file_name}")
        print(f"[INFO] Tamanho total do arquivo: {file_size} bytes")

        pacotes_enviados = 0
        bytes_enviados = 0
        start_time = time.time()

        with open(file_path, "rb") as file:
            while chunk := file.read(1024):
                client_socket.sendto(chunk, (server_host, server_port))
                pacotes_enviados += 1
                bytes_enviados += len(chunk)
                print(f"[ENVIADO] Pacote {pacotes_enviados}: {len(chunk)} bytes | Total enviado: {bytes_enviados} bytes")

        # Enviar indicador de fim de transmissão
        client_socket.sendto(b"EOF", (server_host, server_port))
        pacotes_enviados += 1

        # Recebe o end_time do servidor
        server_time, _ = client_socket.recvfrom(1024)
        end_time = float(server_time.decode())
        total_time = end_time - start_time

        print(f"[ESTATISTICA] Arquivo {file_name} de tamanho {file_size} bytes foi enviado com sucesso.")
        print(f"[ESTATISTICA] Pacotes enviados: {pacotes_enviados}")
        print(f"[ESTATISTICA] Tempo total da transferência: {total_time:.6f} segundos")

    client_socket.close()
    print("[INFO] Conexão com o servidor encerrada.")

if __name__ == "__main__":
    start_udp_client('192.168.1.2', 5001)
