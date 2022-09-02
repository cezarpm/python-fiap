valor1 = int(input("Digite um valor: "))
valor2 = int(input("Digite um valor: "))
valor3 = int(input("Digite um valor: "))

if(valor1 > valor2 and valor1 > valor3):
    print(f"Valor 1 é o maior de todos")
elif(valor2> valor1 and valor2 > valor3):
    print(f"Valor 2 é o maior de todos")
elif(valor3> valor1 and valor3> valor2):
    print(f"Valor 3 é o maior de todos")
