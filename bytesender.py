import socket

def send_bytes(target_ip, target_port, payload):
    # Cria o socket TCP
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Conecta-se ao alvo
        sock.connect((target_ip, target_port))
        
        # Envia os bytes especificados
        sock.send(payload.encode())
        
        print(f"Bytes enviados: {len(payload)}")
    except Exception as e:
        print(f"Erro ao enviar bytes: {e}")
    finally:
        # Fecha o socket
        sock.close()

# Exemplo de uso
target_ip = input("Insira o endereço IP do alvo: ")
target_port = int(input("Insira a porta do alvo: "))
payload = input("Insira os caracteres específicos de bytes a serem enviados: ")

send_bytes(target_ip, target_port, payload)
