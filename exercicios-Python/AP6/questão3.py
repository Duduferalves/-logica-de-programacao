def somar_tres_valores(a, b, c):
    return a + b + c

if __name__ == '__main__':
    print("Este programa soma três números inteiros\n")

    valor1 = int(input("Digite o primeiro número: "))
    valor2 = int(input("Digite o segundo número: "))
    valor3 = int(input("Digite o terceiro número: "))

    resultado = somar_tres_valores(valor1, valor2, valor3)

    print("A soma dos números digitados é:", resultado)

    print("Programa encerrado")
