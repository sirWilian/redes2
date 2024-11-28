#!/bin/bash

apt-get update -y && apt-get upgrade -y

apt-get install -y python3 python3-pip


pip3 install --no-cache-dir --upgrade pip
pip3 install --no-cache-dir requests

echo "Ambiente configurado com sucesso!"
