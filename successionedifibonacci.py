temp = 1
f1 = 0
f2 = 1
print("Quanti numeri vuoi? ")
numerotermini = int(input())
for i in range(0, numerotermini - 1 + 1, 1):
    print(temp)
    temp = f1 + f2
    f1 = f2
    f2 = temp
