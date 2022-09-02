print("-------------- Calculadora --------------")
print("1 - Triângulo")
print("2 - Quadrado")
print("3 - Retângulo")
print("4 - Círculo")
print("5 - Sair")
print("-----------------------------------------")

opcao = int(input("Digite a opção desejada: "))

if (opcao == 1):
    print("Triângulo")
    base = float(input("Digite o valor da base: "))
    altura = float(input("Digite o valor da altura: "))
    print("Área: ", base * altura / 2)

elif (opcao == 2):
    print("Quadrado")
    lado = float(input("Digite o valor do lado: "))
    print("Área: ", lado * lado)

elif (opcao == 3):
    print("Retângulo")
    base = float(input("Digite o valor da base: "))
    altura = float(input("Digite o valor da altura: "))
    print("Área: ", base * altura)

elif (opcao == 4):
    print("Círculo")
    raio = float(input("Digite o valor do raio: "))
    print("Área: ", 3.14 * raio * raio)

elif (opcao == 5):
    print("Sair")

elif (opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4 and opcao != 5):
    print("Opção inválida")
