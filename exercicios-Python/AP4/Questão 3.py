soma = 0
ct = 0
print("-Dobro dos números naturais até 10:")

for n in range(1, 11, 1):
    dobro = n * 2
    print(dobro)
    soma = soma + dobro
    ct = ct + 1

media = soma / ct

print("Soma:", soma)
print("Média:", media)
