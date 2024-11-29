import socket
import time

def start_tcp_server(host='0.0.0.0', port=5000):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Servidor TCP aguardando conexões em {host}:{port}...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Conexão recebida de {client_address}")
        
        # Receber nome do arquivo
        file_name = client_socket.recv(1024).decode()
        print(f"Recebendo arquivo: {file_name}")
        
        # Responder que está pronto para receber
        client_socket.send("READY".encode())
        
        pacotes_recebidos = 0
        # Receber o conteúdo do arquivo e salvá-lo
        with open(file_name, "wb") as file:
            while chunk := client_socket.recv(1024):
                file.write(chunk)
                pacotes_recebidos += 1
                
        # Envia end_time para o cliente
        end_time = time.time()
        client_socket.send(str(end_time).encode())
        
        print(f"Arquivo {file_name} recebido e salvo com sucesso.")
        print(f"Pacotes recebidos: {pacotes_recebidos}")
        
        client_socket.close()

if __name__ == "__main__":
    start_tcp_server()
