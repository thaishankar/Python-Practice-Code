def happy_num(n):
    loop = 1
    sum_digits = 0
    list_sum = []
    
    while loop == 1:
        while (n > 0):
            digit = n%10
            sum_digits += digit * digit
            n = n / 10
 
            
        if sum_digits in list_sum:
            print sum_digits
            return -1
        elif sum_digits == 1:
            return 1
        else:
            list_sum.append(sum_digits)
            
        n = sum_digits
        print sum_digits
        sum_digits = 0
        
if __name__ == '__main__':
    print happy_num(5)
