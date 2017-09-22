def ValidNumber(num):
    num = num.strip()
    ptSeen = 0
    eSeen = 0
    for i in range(len(num)):
        if num[i] == '+' or num[i] == '-':
            if i != 0:
                return -1
        elif num[i] == '.':
            if ptSeen == 1 or eSeen == 1:
                return -1
            else:
                ptSeen =1
        elif num[i] == 'e':
            if eSeen == 1:
                return -1
            else:
                eSeen = 1
        elif not num[i].isdigit():
                return -1

                
    return 1

if __name__ == '__main__':
    num = '-12.3e12'
    print ValidNumber(num)
