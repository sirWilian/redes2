import socket
import time
import os

def start_udp_server(host='0.0.0.0', port=5001):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))
    print(f"Servidor UDP aguardando arquivos em {host}:{port}...")

    while True:
        print("[INFO] Aguardando nome do arquivo ou comando...")
        file_name, client_address = server_socket.recvfrom(1024)
        file_name = file_name.decode().strip()

        if file_name.lower() == "exit":
            print("[INFO] Comando 'exit' recebido. Encerrando conexão com o cliente.")
            break

        if not file_name:
            print("[ERRO] Nome do arquivo inválido ou vazio. Ignorando requisição.")
            continue

        print(f"[INFO] Recebendo arquivo: {file_name} de {client_address}")

        pacotes_recebidos = 0
        bytes_recebidos = 0

        with open(file_name, "wb") as file:
            while True:
                data, _ = server_socket.recvfrom(1024)

                # Verificar indicador de fim de transmissão
                if data == b"EOF":
                    print("[INFO] Final da transmissão recebido.")
                    break

                file.write(data)
                pacotes_recebidos += 1
                bytes_recebidos += len(data)
                print(f"[RECEBIDO] Chunk {pacotes_recebidos}: {len(data)} bytes | Total recebido: {bytes_recebidos} bytes")

        end_time = time.time()

        # Envia end_time para o cliente
        server_socket.sendto(str(end_time).encode(), client_address)

        file_size = os.path.getsize(file_name)
        print(f"[ESTATISTICA] Arquivo {file_name} de tamanho {file_size} bytes recebido e salvo com sucesso.")
        print(f"[ESTATISTICA] Pacotes recebidos: {pacotes_recebidos}")

    print("[INFO] Servidor encerrado.")

if __name__ == "__main__":
    start_udp_server()
