import subprocess

def create_pattern():
    num_bytes = int(input("Digite o número de bytes do padrão: "))
    output = subprocess.check_output(["/usr/share/metasploit-framework/tools/exploit/pattern_create.rb", "-l", str(num_bytes)])
    
    print("\n--- pattern_create ---")
    print("Padrão criado:")
    print(output.decode())

def find_offset():
    num_bytes = int(input("Digite o número de bytes do padrão: "))
    eip_value = input("Digite o valor de EIP encontrado: ")
    output = subprocess.check_output(["/usr/share/metasploit-framework/tools/exploit/pattern_offset.rb", "-l", str(num_bytes), "-q", eip_value])
    
    print("\n*** Encontrando Offset ***")
    print("Offset encontrado:")
    print(output.decode())

def main():
    print("Escolha uma opção:")
    print("1. Criar padrão")
    print("2. Encontrar offset")
    choice = int(input("Opção: "))

    if choice == 1:
        create_pattern()
    elif choice == 2:
        find_offset()
    else:
        print("\n=== Opção inválida. ===")

if __name__ == "__main__":
    main()
