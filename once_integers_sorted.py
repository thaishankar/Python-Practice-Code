def once_integers_sorted(arr):

    res = []
    n = len(arr)
    begin = 0
    res.append(arr[0])
    for i in range(1,n):
        if arr[begin] != arr[i]:
            res.append(arr[i])
            begin = i

    return res


if __name__ == '__main__':
    arr = [1, 2, 2, 2, 3, 3, 4, 5]
    print once_integers_sorted(arr)
