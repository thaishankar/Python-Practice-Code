def isValid(s):

    chars = list(s)
    maps = {'{' : '}', '(' : ')', '[' : ']'} 
    stack = []
    
    for i in range(0, len(chars)):
        if chars[i] in maps:
            stack.append(chars[i])
        elif chars[i] in maps.values() and len(stack) != 0:
            elem = stack.pop()
            if maps[elem] != chars[i]:
                return False
    return True
        
        

if __name__ == '__main__':
    string = "(ablc){as(dag)}"
    if(isValid(string)):
        print "Pattern matches"
    else:
        print "No match"
    
        
