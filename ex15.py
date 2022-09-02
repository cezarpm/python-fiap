v1 = float(input("Digite um valor: "))
v2 = float(input("Digite um valor: "))
v3 = float(input("Digite um valor: "))

if (v1 + v2 > v3) or (v2 + v3 > v1) or (v3 + v1 > v2):
    if (v1 == v2) and (v1 == v3) and (v2 == v3):
        print("Seu triânguo é equilátero!")
    elif (v1 != v2) and (v1 != v3) and (v2 != v3):
        print("Seu triângulo é escaleno!")
    else:
        print("Seu triângulo é isósceles!")
else:
    print("Não é um triângulo.")