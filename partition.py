pentagonal_1 = []
pentagonal_2 = []

for n in range(1000):
    pentagonal_1.append(int((3*n*n-n)/2))
    pentagonal_2.append(int((3*n*n+n)/2))

pentagonal_1=pentagonal_1[1:]
pentagonal_2=pentagonal_2[1:]
#print(pentagonal_1)
#print(pentagonal_2)

number = int(input("Give me an integer: "))
size = number+1

sub_pent_1 = []
sub_pent_2 = []

for i in range(number+1):
    if (pentagonal_1[i] <= number):
        sub_pent_1.append(pentagonal_1[i])
    if (pentagonal_2[i] <= number):
        sub_pent_2.append(pentagonal_2[i])

partition_list_to_number = [1,1]

for n in range(2,size):
    value = 0
    for p in range(len(sub_pent_1)):
        if (sub_pent_1[p] <= n):
            spot = n-sub_pent_1[p]
            if (p%2==1):
                print(spot)
                value += partition_list_to_number[spot]
            elif (p%2==0):
                print(spot)
                value -= partition_list_to_number[spot]
    for p in range(len(sub_pent_2)):
        if (sub_pent_2[p] <= n):
            spot = n-sub_pent_2[p]
            if (p%2==1):
                print(spot)
                value += partition_list_to_number[spot]
            elif (p%2==0):
                print(spot)
                value -= partition_list_to_number[spot]
    partition_list_to_number.append(value)

print(partition_list_to_number)

#print(sub_pent_1)
#print(sub_pent_2)