print("Exibir os 20 primeiros termos da sequência de Bergamaschi")
n = 20
i = 0

v1 = 1
v2 = 1
v3 = 1

while (i <= n):
    if (i <= 2):
        Next = 1
    else:
        Next = v1 + v2 + v3
        v1 = v2
        v2 = v3
        v3 = Next
    print(Next)
    i = i + 1
