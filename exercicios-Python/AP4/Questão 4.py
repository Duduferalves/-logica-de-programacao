ct = 0
fim = int(input("Digite o valor final da sequência: "))
print("-Números naturais até", fim, ":")

for n in range(1, fim + 1, 1):
    print(n)
    ct = ct + 1

print("Total de números:", ct)
