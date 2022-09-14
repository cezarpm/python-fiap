sexo = input("Digite seu sexo: ")

while (sexo.upper() != "M") and (sexo.upper() != "F"):
    print("Sexo não encontrado")
    sexo = input("Digite um sexo válido: ")