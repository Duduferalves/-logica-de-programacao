inicio = int(input("Digite o valor inicial em Fahrenheit: "))
fim = int(input("Digite o valor final em Fahrenheit: "))

print("Fahrenheit | Celsius")
if inicio <= fim:
    for f in range(inicio, fim + 1, 1):
        c = 5 * (f - 32) / 9
        print(f"{f:.1f} ºF | {c:.3f} ºC")
else:
    for f in range(inicio, fim -1, -1):
        c = 5 * (f - 32) / 9
        print(f"{f:.1f} ºF | {c:.3f} ºC")
