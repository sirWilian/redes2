#!/bin/bash

# Caminho do script cliente-udp.py
CLIENT_SCRIPT="cliente-tcp.py"

# Endereço do servidor e porta
SERVER_HOST="192.168.1.2"
SERVER_PORT="5001"

# Arquivo que será enviado
FILE_PATH="Malee Pratas 925.pdf"

# Loop para enviar o arquivo 5 vezes
for i in {1..5}
do
    echo "[INFO] Enviando o arquivo $FILE_PATH - tentativa $i/5"
    
    # Cria um arquivo temporário para simular a entrada do arquivo
    (echo "$FILE_PATH"; echo "exit") | python3 $CLIENT_SCRIPT $SERVER_HOST $SERVER_PORT
    
    # Pausa de 2 segundos entre os envios (opcional)
    sleep 2
done

echo "[INFO] Todos os envios foram realizados."
