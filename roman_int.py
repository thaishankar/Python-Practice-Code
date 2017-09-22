"""
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
"""

def roman_to_int(num):
        d = {}
        d['I'] = 1
        d['V'] = 5
        d['X'] = 10
        d['L'] = 50
        d['C'] = 100

        n = len(num)
        s = d[num[n-1]]
        for i in range(n-2, -1, -1):
                if (num[i] < num[i+1]):
                    s -= d[num[i]]
                else:
                    s += d[num[i]]
        return s

        
if __name__ == '__main__':
    roman = "XIV"
    print roman_to_int(roman)
