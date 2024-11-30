import socket
import time

def start_udp_server(host='0.0.0.0', port=5001):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))
    print(f"Servidor UDP aguardando arquivos em {host}:{port}...")

    while True:
        print("Aguardando nome do arquivo...")
        file_name, client_address = server_socket.recvfrom(1024)
        file_name = file_name.decode()
        print(f"Recebendo arquivo: {file_name} de {client_address}")

        pacotes_recebidos = 0
        with open(file_name, "wb") as file:
            while True:
                data, _ = server_socket.recvfrom(1024)
                pacotes_recebidos += 1
                # Verificar se é o indicador de fim de transmissão
                if data == b"EOF":
                    print(f"Arquivo {file_name} recebido com sucesso.")
                    break
                file.write(data)
        end_time = time.time()

        # Enviar confirmação ao cliente
        response = f"Arquivo {file_name} recebido com sucesso."
        server_socket.sendto(response.encode(), client_address)
        
        # Envia end_time para o cliente
        server_socket.sendto(str(end_time).encode(), client_address)
        
        print(f"Pacotes recebidos: {pacotes_recebidos}")

if __name__ == "__main__":
    start_udp_server()
