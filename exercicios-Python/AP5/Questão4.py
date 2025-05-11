soma = 0
for n in range(1, 501, 1):
    if n % 2 != 0 and n % 3 == 0:
        soma = soma + n
print("Soma dos números ímpares e múltiplos de 3 de 1 a 500:", soma)
