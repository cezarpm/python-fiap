tabuada_atual = 1

while(tabuada_atual <= 20):
  multiplicador = 0
  while(multiplicador <= 10):
    print(f"{tabuada_atual} x {multiplicador} = {tabuada_atual * multiplicador}")
    multiplicador = multiplicador + 1
  tabuada_atual = tabuada_atual + 1
  input("Pressione para continuar.......")