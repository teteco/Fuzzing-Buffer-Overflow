def mona_jmp():
    print("\n=== Encontrar endereço para JMP ESP ===")
    print("No Immunity Debugger, utilize o seguinte comando:")
    print("\n!mona jmp -r esp")
    print("\nExplicação:")
    print("- Esse comando busca por um endereço que contém a instrução 'JMP ESP'.")
    print("- Use esse endereço para redirecionar a execução do programa após explorar o buffer overflow.")
    print("\nCertifique-se de que o módulo onde você encontrou o endereço não possui proteções como DEP ou ASLR.")

def mona_bytearray():
    print("\n=== Gerar bytearray para detectar badchars ===")
    print("No Immunity Debugger, utilize o seguinte comando:")
    print('\n!mona bytearray -cpb "\\x00"')
    print("\nExplicação:")
    print("- Esse comando gera um array de bytes excluindo o caractere nulo '\\x00'.")
    print("- Compare o bytearray gerado com o conteúdo da memória após o overflow para identificar badchars adicionais.")
    print("\nDica: Adicione mais caracteres à lista '-cpb' conforme você encontrar novos badchars.")

def main():
    print("Escolha uma opção:")
    print("1. Executar comando para encontrar JMP ESP")
    print("2. Executar comando para gerar bytearray")
    
    choice = input("Opção (1 ou 2): ").strip()
    
    if choice == "1":
        mona_jmp()
    elif choice == "2":
        mona_bytearray()
    else:
        print("\n[!] Opção inválida. Tente novamente.")

if __name__ == "__main__":
    print("=== Script de Auxílio para Uso do Mona no Immunity Debugger ===")
    main()
