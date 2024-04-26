
def print_fibo(num):
    a = 0
    b = 1
    print(a)
    print(b)
    for i in range(2, num):
        c = a + b
        a = b
        b = c
        print(c)


number = int(input("Enter the range: "))
print_fibo(number)
