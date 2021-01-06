fib = [0, 1]
n = int(input('Enter your number: '))
for i in range(2, n):
    fib.append(fib[i-1]+fib[i-2])

print('Your fibonacci list:', fib)