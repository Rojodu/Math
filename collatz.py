
#Collatzerizer
def collatzerize(test_number):

    hold_num = test_number
    path = [test_number]
    step_count = 0

    while hold_num > 1:
        if hold_num % 2 == 0:
            hold_num/=2
            path.append(int(hold_num))
            step_count+=1
        elif hold_num % 2 == 1:
            hold_num= 3*hold_num + 1
            path.append(int(hold_num))
            step_count+=1
        else :
            hold_num = 0
            path.append(hold_num)
            
    return path