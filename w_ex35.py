tabuada = int(input("Digite a tabuada que vc deseja exibir: "))
tabuada_atual = 1

while (tabuada < 0):
    tabuada = int(input("Digite a tabuada que vc deseja exibir: "))


while(tabuada_atual > 0 and tabuada_atual < 11):
    print(tabuada * tabuada_atual)
    tabuada_atual = tabuada_atual + 1