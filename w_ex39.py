n = 30
i = 0
v1 = 0
v2 = 1

while (i < n):
    if (i <= 1):
        Next = i
    else:
        Next = v1 + v2
        v1 = v2
        v2 = Next
    print(Next)
    i = i + 1
