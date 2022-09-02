peso = float(input("Digite um valor: "))
altura = float(input("Digite um valor: "))

sexo = input("Digite o seu sexo: m ou f: ")

imc = peso / (altura * altura)

if (sexo == "m"):
    if (imc < 20):
        print("Abaixo do peso")
    elif (imc > 20 and imc < 25):
        print("Peso ideal")
    elif (imc > 25):
        print("Acima do peso")

elif (sexo == "f"):
    if (imc < 19):
        print("Abaixo do peso")
    elif (imc > 19 and imc < 24):
        print("Peso ideal")
    elif (imc > 24):
        print("Acima do peso")
