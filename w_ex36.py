tabuada = int(input("Digite"))

while (tabuada < 0):
    tabuada = int(input("Digite o valor A :"))

a = int(input("Qual é o começo da tabuada:  "))
b = int(input("Qual o final da tabuada:  "))

while (a > b):
    b = int(input("Qual é o final da tabuada:  "))

while (a < b):
    print(tabuada * b)
    b = b - 1
