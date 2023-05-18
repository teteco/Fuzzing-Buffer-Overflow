def generate_badchars():
    badchars = []

    for num in range(256):
        badchars.append(hex(num).replace('0x', '\\x'))

    return badchars

# Exemplo de uso
badchars = generate_badchars()

# Exibindo a lista de badchars
print("Lista de Bad Chars:")
for char in badchars:
    print(char, end=' ')

