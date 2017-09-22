
def lonely_pixel(mat, N):
    col_count = len(mat[0])
    row_count = len(mat)

    row = [0] * row_count
    col = [0] * col_count

    for i in range(row_count):
        for j in range(col_count):
            if mat[i][j] == 'B':
                row[i] += 1
                col[j] += 1

    count = 0
    for i in range(row_count):
        for j in range(col_count):
            if row[i] == col[j] and row[i] == N:
                count += N
                col[j] = -1
    return count

if __name__ == '__main__':
    mat = [['W', 'B', 'W', 'B', 'B', 'W'],    
          ['W', 'B', 'W', 'B', 'B', 'W'],    
          ['W', 'B', 'W', 'B', 'B', 'W'],    
          ['W', 'W', 'B', 'W', 'B', 'W']]
    N = 3
    print lonely_pixel(mat, N)
