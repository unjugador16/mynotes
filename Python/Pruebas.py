from random import randint
var1 = 0
var2 = 0
var3 = 0
for _ in range(1,100):
    i = randint(1,3)
    if i == 1:
        var1 += 1
    if i == 2:
        var2 += 1
    if i == 3:
        var3 += 1

print(var1, var2 , var3)