def calcular_salario(horas, valor_hora):
    salario = horas * valor_hora
    return salario

if __name__ == '__main__':
    print("Este programa calcula o salário de uma pessoa\n")

    horas_trabalhadas = float(input("Quantas horas foram trabalhadas? "))
    valor_hora = float(input("Qual o valor da hora trabalhada? "))

    salario_total = calcular_salario(horas_trabalhadas, valor_hora)

    print("O salário calculado é: R$", salario_total)

    print("Cálculo finalizado")

