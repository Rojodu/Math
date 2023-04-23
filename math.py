
#Factorizer
import math

test_number = int(input("Give me a test number: "))

hold_num = math.floor((test_number+1)/2)

factors = [1]
prime_factors = []

for i in range(2,hold_num+1):
    if test_number%i == 0:
        factors.append(i)

factors.append(test_number)
test_factors = factors[1:]

for number in test_factors:
    add = True
    for i in test_factors:
        if (number % i == 0) and (number != i):
            add = False
    if add == True:
        prime_factors.append(number)

print("Factors of",test_number,":", factors,"with",len(factors),"factors")
print("Prime Factors of",test_number,":",prime_factors,"with",len(prime_factors),"prime factors")