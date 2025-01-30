number = int(input("Number: "))


a, b = 0, 1

for _ in range(number):
    print(a, end=" ")
    a, b = b, a + b
