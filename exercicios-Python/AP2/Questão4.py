num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
print("Escolha a operação:")
print("+ para adição")
print("- para subtração")
print("* para multiplicação")
print("/ para divisão")
operacao = input("Digite a operação desejada: ")
if operacao == "+":
    resultado = num1 + num2
    print("Resultado:", resultado)
elif operacao == "-":
    resultado = num1 - num2
    print("Resultado:", resultado)
elif operacao == "*":
    resultado = num1 * num2
    print("Resultado:", resultado)
elif operacao == "/":
    resultado = num1 / num2
    print("Resultado:", resultado)
else:
    print("Operação inválida! Escolha entre +, -, * ou /.")