def most_freq(arr):
    d = {}
    for i in range(len(arr)):
        if arr[i] in d:
            d[arr[i]] = d[arr[i]] + 1
        else:
            d[arr[i]] = 1

    max_count = 0
    max_key = -1
    for key in d:
        if d[key] > max_count:
            max_count = d[key]
            max_key = key
    return max_key
                        

if __name__ == '__main__':
    arr = [1,1,3,4,3,4,5,3,5,3]
    print most_freq(arr)
