
def kill_process(pid, ppid, kill):

    d = {}
    for i in range(len(pid)):
        process = pid[i]
        parent = ppid[i]
        if parent in d:
            d[parent] += [process]
        else:
            d[parent] = [process]

    print d
    q = []
    res = []
    if kill in d:
        q.append(kill)
        res.append(kill)
        while q:
            first = q.pop()
            if first in d:
                all_child = d[first]
                for child in all_child:
                    q.append(child)
                    res.append(child)
    return res

if __name__ == '__main__':
    pid =  [1, 3, 10, 5,]
    ppid = [3, 0, 5, 3]
    kill = 10
    print kill_process(pid, ppid, kill)
