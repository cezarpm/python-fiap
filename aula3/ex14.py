peso = float(input("Digite um valor: "))
altura = float(input("Digite um valor: "))

imc = peso / (altura * altura)

if(imc< 19):
    print("Abaixo do peso")
elif (imc > 19 and imc < 24):
    print("Abaixo ideal")
elif (imc< 24):
    print("Acima do peso")