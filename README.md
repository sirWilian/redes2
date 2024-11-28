# redes2


# Rede Docker: Configuração de Cliente-Servidor TCP/UDP

Este projeto configura um ambiente Docker com duas máquinas baseadas em Ubuntu para testar a comunicação TCP e UDP. Cada máquina está pré-configurada para executar scripts Python de interação cliente-servidor.

## Estrutura do Projeto

```
.
├── docker-compose.yml      # Arquivo Docker Compose para configurar o ambiente
├── volumes/
│   ├── maquina1/                   # Diretório montado na maquina1
│   │   ├── servidor-tcp.py   
│   │   ├── servidor-udp.py   
│   │   ├── setup_environment.sh    # Script para configurar dependências
│   ├── maquina2/                   # Diretório montado na maquina2
│       ├── cliente-tcp.py   
│       ├── cliente-udp.py   
│       ├── setup_environment.sh    # Script para configurar dependências
```

---

## Pré-requisitos

- Docker instalado no seu sistema.
- Conhecimentos básicos de Docker e Python.

---

## Instruções de Configuração

### 3. Inicie o Ambiente Docker

Execute o seguinte comando para iniciar os containers:

```bash
docker-compose up -d
```

---

## Acessando as Máquinas

### Acessar maquina1

```bash
docker exec -it maquina1 bash
```

### Acessar maquina2

```bash
docker exec -it maquina2 bash
```

---

## Testando a Comunicação TCP

1. **Inicie o Servidor TCP** na `maquina1`:
   ```bash
   python3 servidor-tcp.py
   ```
2. **Execute o Cliente TCP** na `maquina2`:
   ```bash
   python3 cliente-tcp.py
   ```

---

## Testando a Comunicação UDP

1. **Inicie o Servidor UDP** na `maquina1`:
   ```bash
   python3 servidor-udp.py
   ```
2. **Execute o Cliente UDP** na `maquina2`:
   ```bash
   python3 cliente-udp.py
   ```

---

## Parando os containers

Para parar e remover os containers e a rede, execute:

```bash
docker-compose down
```

---

## Notas

- O script `setup_environment.sh` instala automaticamente o Python e as dependências (como `pip`) em cada container ao iniciar.
- Se você modificar os scripts ou adicionar novos, reinicie os containers usando:
  ```bash
  docker-compose restart
  ```
