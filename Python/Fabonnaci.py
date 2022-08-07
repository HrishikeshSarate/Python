num = int(input("Enter the Number:"))

a, b = 0, 1

print("Fibonacci Series:", a,",", b, end=" , ")

for i in range(2, num):

    c = a + b

    a = b

    b = c

    print(c,",", end=" ")