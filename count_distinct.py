def count_distinct(l, k):
    i =1
    d = {}
    for key in l:
        print key, i
        if key in d:
            val = d[key]
            val = val + 1
            d[key] = val
        else:
            d[key] = 1

        if i>k:
            val = d[l[i-k]]
            val = val - 1
            d[l[i-k]] = val
            if val == 0:
                del d[l[i-k]]
            print ("For %s: %s" %((i-k), len(d.keys())))
        i = i + 1                

if __name__ == '__main__':
    l = [1, 2, 1, 3, 4, 2, 3]
    k = 4
    count_distinct(l, k)
