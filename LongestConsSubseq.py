
def findLongestConseqSubseq(arr, n):
    h = []
    ans = 0
    j = 0
    for i in range(0, n):
        h.append(arr[i])
    print h

    for i in range(0, n):
        if (arr[i] - 1) not in h:
            print arr[i]
            j = arr[i]
            while(j in h):
                j = j + 1
                
            if ans < j - arr[i]:
                ans = j - arr[i]
    return ans
        
 
# Driver function 
if __name__=='__main__':
    n = 7
    arr = [1, 9, 3, 10, 4, 20, 2]
    print "Length of the Longest contiguous subsequence is %s" % findLongestConseqSubseq(arr, n)
         
