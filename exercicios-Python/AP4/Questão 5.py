ct = 0
inicio = int(input("Digite o valor inicial da sequência: "))
print("-Números naturais na ordem decrescente até 0:")

for n in range(inicio, -1, -1):
    print(n)
    ct = ct + 1

print("Quantidade de números:", ct)
