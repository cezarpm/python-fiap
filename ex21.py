n1 = float(input("Digite um valor: "))
n2 = float(input("Digite um valor: "))

print("-------------- Calculadora --------------")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
print("5 - Sair")
print("-----------------------------------------")

opcao = int(input("Digite a opção desejada: "))

if (opcao == 1):
    print("Soma")
    print(n1 + n2)
    print("----------- Fim do programa -------------")

elif (opcao == 2):
    print("Subtração")
    print(n1 - n2)
    print("----------- Fim do programa -------------")

elif (opcao == 3):
    print("Multiplicação")
    print(n1 * n2)
    print("----------- Fim do programa -------------")

elif (opcao == 4):
    if (n2 == 0):
        print("Divisão por zero")
        print("----------- Fim do programa -------------")

    print("Divisão")
    print(n1 / n2)
    print("----------- Fim do programa -------------")

elif (opcao == 5):
    print("Sair")
    print("----------- Fim do programa -------------")

elif (opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4 and opcao != 5):
    print("Opção inválida")
