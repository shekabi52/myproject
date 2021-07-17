# reverse an integer
num = 101
num1 = 0
while (num != 0):
    n = num % 10
    num1 = num1 * 10 + n
    num = num // 10

print(num1)
# floor quotient
print(20 // 10)
# exponential
print(2 ** 5)
a = 10
b = 20
c = 30
# largest number
if (a > b and b > c):
    print(a, " is larger")
elif (b > a and b > c):
    print(b, " is larger")
else:
    print(c, " is larger")

print(24 // 6)

a1 = 5
b1 = 5
print(a1 is not b1)

l1 = [1, 2, 3, 4, 5]
l2 = [2, 5, 1, 8, 4]

for i in l1:
    for j in l2:
        if (i == j):
            print(i, sep="*", end="")

print("")
row = 5

for i in range(0, row + 1):
    for j in range(0, i):
        print("*", end="")
    print(" ")

print()
print()
for i in range(1, row + 1):
    for j in range(0, row - i):
        print(" ", end="")
    for j in range(1, 2 * i):
        print("*", end="")
    print()
# reverse an integer
num = 101
num1 = 0
while (num != 0):
    n = num % 10
    num1 = num1 * 10 + n
    num = num // 10

print(num1)
# floor quotient
print(20 // 10)
# exponential
print(2 ** 5)
a = 10
b = 20
c = 30
# largest number
if (a > b and b > c):
    print(a, " is larger")
elif (b > a and b > c):
    print(b, " is larger")
else:
    print(c, " is larger")

print(24 // 6)

a1 = 5
b1 = 5
print(a1 is not b1)

l1 = [1, 2, 3, 4, 5]
l2 = [2, 5, 1, 8, 4]

for i in l1:
    for j in l2:
        if (i == j):
            print(i, sep="*", end="")

print("")
row = 5

for i in range(0, row + 1):
    for j in range(0, i):
        print("*", end="")
    print(" ")

print()
print()
for i in range(1, row + 1):
    for j in range(0, row - i):
        print(" ", end="")
    for j in range(1, 2 * i):
        print("*", end="")
    print()

class test:
    def __init__(self,name):
        self.name=name
    def fun(self):
        print('i am a function {name}'.format(self.name))


t=test("abishek")
t.fun()