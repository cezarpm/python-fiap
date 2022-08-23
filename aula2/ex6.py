valor_produto1 = int(input("Digite o valor do produto 1: "))
valor_produto2 = int(input("Digite o valor do produto 2: "))
valor_produto3 = int(input("Digite o valor do produto 3: "))
valor_produto4 = int(input("Digite o valor do produto 4: "))

valor_total =  valor_produto1 + valor_produto2 + valor_produto3 + valor_produto4

print("O valor total em reais é: R$" , valor_total)

valor_pago = int(input("Digite o valor a ser pago: "))

valor_troco =  valor_pago - valor_total  

print("O valor do troco é", valor_troco)