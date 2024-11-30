import socket
import time
import os 

def start_tcp_server(host='0.0.0.0', port=5001):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Servidor TCP aguardando conexões em {host}:{port}...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"[INFO] Conexão recebida de {client_address}")

        while True:
            # Receber nome do arquivo ou comando
            data = client_socket.recv(1024).decode()

            if data.lower() == "exit":
                print("[INFO] Comando 'exit' recebido. Encerrando conexão com o cliente.")
                client_socket.close()
                break
            
            if not data:
                continue
            
            if not data.strip():  # Ignora entradas vazias
                print("[INFO] Dados inválidos ou vazios recebidos.")
                continue

            print(f"[INFO] Recebendo arquivo: {data}")
            file_name = data

            # Responder que está pronto para receber
            client_socket.send("READY".encode())
            print(f"[INFO] Servidor pronto para receber!")

            pacotes_recebidos = 0
            bytes_recebidos = 0

            # Receber o conteúdo do arquivo e salvá-lo
            with open(file_name, "wb") as file:
                print("[INFO] Recebendo arquivo...")    

                while chunk := client_socket.recv(1024):
                    if chunk.endswith(b"END"):
                        # Remover o "END" do chunk
                        chunk = chunk[:-3]
                        if chunk:  # Escreve os dados restantes, se houver
                            file.write(chunk)
                        print("[INFO] Final da transmissão recebido.")
                        break
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

        print(f"[INFO] Conexão encerrada com {client_address}")

if __name__ == "__main__":
    start_tcp_server()
