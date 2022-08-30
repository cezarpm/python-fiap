base = int(input("Digite um valor: "))
altura = int(input("Digite um valor: "))

area = base * altura

if(area > 100):
    print(f"Terreno grande")

if(area < 100):
    print(f"Terreno pequeno")

print(f"A área do retângulo é: {area}")


