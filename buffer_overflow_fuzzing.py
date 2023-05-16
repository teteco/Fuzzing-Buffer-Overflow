import socket

# Solicita ao usuário o endereço IP e a porta do alvo
target_ip = input("Insira o endereço IP do alvo: ")
target_port = int(input("Insira a porta do alvo: "))

# Lista de caracteres para fuzzing
fuzz_chars = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
              'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# Loop de fuzzing
for char in fuzz_chars:
    # Cria um payload com o caractere repetido várias vezes
    payload = char * 1000
    
    # Cria o socket TCP
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        # Conecta-se ao alvo
        sock.connect((target_ip, target_port))
        
        # Envie o payload
        sock.send(payload.encode())
        
        # Aguarde a resposta (opcional)
        response = sock.recv(1024)
        
        # Verifique se há comportamento anormal na resposta (opcional)
        if "crash" in response.decode():
            print(f"Encontrada uma possível vulnerabilidade com o caractere: {char}")
    except:
        print(f"Não foi possível conectar-se ao alvo: {target_ip}:{target_port}")
    
    # Fecha o socket
    sock.close()
