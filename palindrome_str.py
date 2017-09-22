def palindrome_str(l):
    for s in l:
        length = len(s)
        flag = 0
        for i in range(0, length/2):
            print i
            if s[i] != s[length - i -1]:
                flag = 1
                break
        if not flag:
            print s


if __name__ == '__main__':
    l = ['abcba','def','a','abcde','abba']
    palindrome_str(l)
    
