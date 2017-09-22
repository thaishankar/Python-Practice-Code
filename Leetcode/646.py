def findLongestChain(pairs):
    pairs.sort()
    pairs = sorted(pairs, key=lambda x: x[1])
    print pairs
    
    l = 1
    prev_end = pairs[0][1]
    for pair in pairs:
        if prev_end < pair[0]:
            l += 1
            prev_end = pair[1]
    return l

if __name__ == '__main__':
    pairs = [[-6,9],[1,6],[8,10],[-1,4],[-6,-2],[-9,8],[-5,3],[0,3]]
    
    print findLongestChain(pairs)
