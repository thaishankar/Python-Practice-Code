
def increment_key(arr, d, i, count):
    if arr[i] not in d:
        d[arr[i]] = count
    else:
        c = d[arr[i]]
        c = c + count
        d[arr[i]] = c

def distinct_k(arr, k):
    l = len(arr)
    d = {}
    for i in range(0, l):
        if ( i < k):
            increment_key(arr, d, i, 1)
        else:
            #decrement count of i-k
            # increment count of current element
            c = d[arr[i-k]]
            c = c - 1
            if arr[i-k] in d and c == 0:
                del d[arr[i-k]]
            else:
                d[arr[i-k]] = c

            increment_key(arr, d, i, 1)

        if (i >= k-1):
            print len(d)



if __name__ == '__main__':
        arr = [1, 2, 1, 3, 4, 2, 3]
        k = 4
        distinct_k(arr, k)
