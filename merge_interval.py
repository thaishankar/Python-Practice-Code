
def insert_and_merge_interval(l, interval):

    for i in range(len(l)):
        start = l[i][0]
        if interval[0] < start:
            break
        
    if i == len(l)-1 and start < interval[0]:
        l.append(interval)
        i = len(l) - 1
    else:
        l.insert(i, interval)

    merge_overlapping(l, i)

def merge_overlapping(l, i):
    elem = l[i]
    print elem
    
    #merge left
    for pos in range(i, -1, -1):
       if pos > 0 and elem[0] < l[pos][1]:
  

if __name__ == '__main__':
    l = [(-10, 1), (0, 2), (4, 10)]
    insert_and_merge_interval(l, (-5, 1))
