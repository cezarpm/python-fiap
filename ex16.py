v1 = float(input("Digite um valor: "))
v2 = float(input("Digite outro valor: "))
v3 = float(input("Digite mais um valor: "))

if (v1 == (v2**2 + v3**2)/v1) or (v3 == (v2**2 + v1**2)/v3) or (v2 == (v3**2 + v1**2)/v2):
    print("Seu triângulo é retângulo!")
else:
    print("Seu triângulo não é retângulo!")