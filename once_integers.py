def once_integers(arr):

    d = {}
    res = []
    for i in range(len(arr)):
        if arr[i] in d:
            d[arr[i]] += 1
        else:
            d[arr[i]] = 1

    print d
    for key in d:
        if d[key] == 1:
            res.append(key)
    return res

if __name__ == '__main__':
    arr = [1, 2, 3, 5, 2, 2, 3, 4]
    print once_integers(arr)
