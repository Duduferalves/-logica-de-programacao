a = float(input("Digite o comprimento do primeiro lado (a): "))
b = float(input("Digite o comprimento do segundo lado (b): "))
c = float(input("Digite o comprimento do terceiro lado (c): "))
if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("É um triângulo equilátero.")
    elif a == b or b == c or a == c:
        print("É um triângulo isósceles.")
    else:
        print("É um triângulo escaleno.")
else:
    print("Não é um triângulo.")