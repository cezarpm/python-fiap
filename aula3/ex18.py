valor_aceleracao = float(input("Digite um valor: "))
velocidade_inicial = float(input("Digite um valor: "))
tempo_percurso = float(input("Digite um valor: "))

velocidade_final = (velocidade_inicial + valor_aceleracao * tempo_percurso) * 3.6

print(velocidade_final)

if(velocidade_final <= 40):
    print("Veículo muito lento")
elif(velocidade_final > 40 and velocidade_final <= 60):
    print("Velocidade permitido")
elif(velocidade_final > 60 and velocidade_final <= 80):
    print("Velocidade de cruzeiro")
elif(velocidade_final > 80 and velocidade_final <= 120):
    print("Veículo rápido")
elif velocidade_final > 120:
    print("Rapidão")
