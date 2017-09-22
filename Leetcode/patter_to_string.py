pattern = "abba"
word = "dog cat ps dog"

def pattern_checker(pattern, word):
    words = word.split()
    pattern = list(pattern)
    if len(words) != len(pattern):
        return False

    p2w = {}
    w2p = {}
    for i in range(0, len(words)):
        w = words[i]
        p = pattern[i]
        print p, w
        if p in p2w and w in w2p:
            if p2w[p] != w or w2p[w] != p:
                return False

        elif p in p2w or w in w2p:
            return False

        else:
            p2w[p] = w
            w2p[w] = p



    return True

if __name__ == '__main__':
    if(pattern_checker(pattern, word)):
        print "Pattern matches"
    else:
        print "No match"
    
        
