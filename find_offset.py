import subprocess

def find_offset():
    # Solicitar o número de bytes usados para gerar o padrão
    num_bytes = int(input("Digite o número de bytes do padrão: "))
    
    # Solicitar o valor do EIP que foi encontrado
    eip_value = input("Digite o valor de EIP encontrado: ")
    
    # Executar o comando pattern_offset.rb
    output = subprocess.check_output(
        ["/usr/share/metasploit-framework/tools/exploit/pattern_offset.rb", "-l", str(num_bytes), "-q", eip_value]
    )
    
    # Exibir o offset encontrado
    print("\n*** Encontrando Offset ***")
    print("Offset encontrado:")
    print(output.decode())

if __name__ == "__main__":
    find_offset()
