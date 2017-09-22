def isomorphic(s, t):
    d1 = {}
    d2 = {}
    l1 = len(s)
    l2 = len(t)
    
    if l1 != l2:
        return False

    for i in range(l1):
        s_ch = s[i]
        t_ch = t[i]
        print s_ch, t_ch
        if s_ch in d1 and t_ch in d2:
            if s_ch != d2[t_ch] or t_ch != d1[s_ch]:
                print "mismatch: %s:%s %s:%s " % (s_ch, d1[s_ch], t_ch, d2[t_ch])
                return False
        elif s_ch in d1 or t_ch in d2:
            return False
        else:
            d1[s_ch] = t_ch
            d2[t_ch] = s_ch
            
    return True



if __name__ == '__main__':
    s = "aa"
    t = "bb"
    res = isomorphic(s, t)
    print res
