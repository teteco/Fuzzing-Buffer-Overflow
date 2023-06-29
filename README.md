# Fuzzing-Buffer-Overflow

Este código Python é um exemplo básico de um programa de fuzzing para testar uma aplicação em busca de vulnerabilidades de buffer overflow.

Ele solicita ao usuário que insira o endereço IP e a porta do alvo. Em seguida, um loop de fuzzing é executado, onde uma lista de caracteres é iterada. Para cada caractere, um payload é criado repetindo o caractere várias vezes.

O programa cria um socket TCP e tenta conectar-se ao alvo usando o endereço IP e a porta fornecidos. Em seguida, o payload é enviado para o alvo. O código inclui comentários para indicar que é possível aguardar a resposta do alvo e verificar se há comportamentos anormais na resposta.

É importante ressaltar que este exemplo é apenas uma base e pode ser aprimorado para atender às necessidades específicas do projeto. Além disso, é fundamental entender as implicações de segurança ao realizar testes de fuzzing e obter as devidas permissões e autorizações antes de executar qualquer código em sistemas ou aplicativos de terceiros.

Ordem recomendada para utilizaçao 
fuzzing.py > pattern_tool.py > send_bytes.py > payload_shellcode.py > exploit_tool.py
