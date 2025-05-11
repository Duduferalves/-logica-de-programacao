altura = float(input("Digite sua altura em metros: "))
sexo = input("Digite seu sexo,'homem' ou 'mulher': ")
if sexo=="homem":
    peso_ideal = (72.7 * altura) - 58
    print("Peso ideal:", peso_ideal)
if sexo == "mulher":
    peso_ideal = (62.1 * altura) - 44.7
    print("Peso ideal:", peso_ideal)
