d = { }
def symmetric_pairs(pairs):
    for p in pairs:
        if p[1] in d:
            if d[p[1]] == p[0]:
                 return p
        else:          
            d[p[0]] = p[1]

if __name__ == '__main__':
    pairs = [(11, 20), (30, 40), (5, 10), (40, 31), (10, 15)]
    print symmetric_pairs(pairs)
