nome = input("Digite seu nome: ")
sexo = input("Digite seu sexo (M/F): ")
estado_civil = input("Digite seu estado civil (S/C/V/D): ")

if (sexo == "F" and estado_civil == "C"):
    tempo_casada = input("Digite o tempo de casada: ")
    print(f"{nome} - {sexo} - {estado_civil} - {tempo_casada}")
else:
    print(f"{nome} - {sexo} - {estado_civil}")
