
def queue_reconstruct(arr):

    peopledict = {}
    height = []
    result = []
    for i in range(len(arr)):
        p = arr[i]
        if p[0] in  peopledict:
            peopledict[p[0]] += [(p[1], i),]
        else:
            peopledict[p[0]] = [(p[1], i)]
            height.append(p[0])

    print peopledict
    height.sort()

    for h in height[::-1]:
        peopledict[h].sort()
        print h, peopledict[h]
        for p in peopledict:
            result.insert(p[0], arr[p[1]])
    return result
            



if __name__ == '__main__':
    arr = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
    print queue_reconstruct(arr)
    
