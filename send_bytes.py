import socket
import sys

def send_data(ip, port):
    # Cria um objeto socket TCP/IP
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Conecta ao endereço e porta fornecidos
    server_address = (ip, port)
    sock.connect(server_address)

    try:
        # Obtém o número de bytes para a letra A
        print("---")
        bytes_a = int(input("Insira o número de bytes para A: "))

        # Obtém o número de bytes para a letra B
        print("---")
        bytes_b = int(input("Insira o número de bytes para B: "))

        # Concatena os bytes A e B
        data = 'A' * bytes_a + 'B' * bytes_b

        # Envia os dados para o endereço IP e porta
        sock.sendall(data.encode())
        print("---")
        print("Bytes enviados: {0}".format(len(data)))
    finally:
        # Fecha a conexão
        sock.close()

if __name__ == "__main__":
    # Verifica se o número correto de argumentos foi fornecido
    if len(sys.argv) != 3:
        print("Uso: python programa.py IP PORTA")
        print("Exemplo: python programa.py 192.168.0.1 8080")
        sys.exit(1)

    # Obtém os argumentos da linha de comando
    ip = sys.argv[1]
    port = int(sys.argv[2])

    # Chama a função para enviar os dados
    send_data(ip, port)
