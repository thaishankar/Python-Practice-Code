def roman_to_int(num):
        num = num.upper()
        s = 0
        if "IV" in num:
            s -= 2
        if "IX" in num:
            s -= 2
        if "XL" in num:
            s -= 20
        if "XC" in num:
            s -= 20

        for i in range(len(num)):
            if num[i] == 'I':
                s += 1
            if num[i] == 'V':
                s += 5
            if num[i] == 'X':
                s += 10
            if num[i] == 'L':
                s += 50
            if num[i] == 'C':
                s += 100
            else:
                return -1

        return s
if __name__ == '__main__':
    roman = "abc"
    print roman_to_int(roman)
