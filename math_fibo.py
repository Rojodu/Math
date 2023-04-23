
#Generating the fibonacci sequence

fib = []

for x in range(100):
    if x == 0 or x == 1:
        fib.append(1)
    else:
        fib.append(fib[x-1]+fib[x-2])

print(fib)