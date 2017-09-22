
def unique_rows(M):
    row = len(M)
    col = len(M[0])
    h = {}

    for i in range(0, row):
        val = 0
        for j in range (0, col):
            val = val + M[i][j] * 2**(col-j-1)
        if not val in h.keys():
            print i
            h[val] = 1
    print h
        
        

if __name__ == '__main__':
    M = [[0, 1, 0, 0, 1], [1, 0, 0, 0 ,1], [0, 1, 0, 0, 1], [1, 1, 0, 0, 0]]
    unique_rows(M)
