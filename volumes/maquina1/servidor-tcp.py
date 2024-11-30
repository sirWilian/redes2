import socket
import time
import os 

def start_tcp_server(host='0.0.0.0', port=5000):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Servidor TCP aguardando conexões em {host}:{port}...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"[INFO] Conexão recebida de {client_address}")
        
        # Receber nome do arquivo
        file_name = client_socket.recv(1024).decode()
        print(f"[INFO] Recebendo arquivo: {file_name}")
        
        # Responder que está pronto para receber
        client_socket.send("READY".encode())
        print(f"[INFO] Servidor pronto para receber!")

        pacotes_recebidos = 0
        bytes_recebidos = 0

        # Receber o conteúdo do arquivo e salvá-lo
        with open(file_name, "wb") as file:
            print("[INFO] Recebendo arquivo...")    
            
            while chunk := client_socket.recv(1024):
                file.write(chunk)
                pacotes_recebidos += 1
                bytes_recebidos += len(chunk)
                print(f"[RECEBIDO] Chunk {pacotes_recebidos}: {len(chunk)} bytes | Total recebido: {bytes_recebidos} bytes")         
        
        # Envia end_time para o cliente
        end_time = time.time()
        client_socket.send(str(end_time).encode())
        file_size = os.path.getsize(file_name)

        print(f"[ESTATISTICA] Arquivo {file_name} de tamanho {file_size} recebido e salvo com sucesso.")
        print(f"[ESTATISTICA] Pacotes recebidos: {pacotes_recebidos}")
        
        client_socket.close()
        print(f"[INFO] conexao encerrada")
        return
if __name__ == "__main__":
    start_tcp_server()
