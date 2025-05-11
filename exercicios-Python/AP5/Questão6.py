num = int(input("Digite o número para ver a tabuada: "))
for n in range(1, 11, 1):
    resultado = n * num
    print(n, "x", num, "=", resultado)
