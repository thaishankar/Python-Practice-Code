def compareVersion(version1, version2):
    """
    :type version1: str
    :type version2: str
    :rtype: int
    """

    n1 = ""
    n2 = ""
    ln1 = len(version1)
    ln2 = len(version2)

    for i in range(0, ln1):
        if version1[i].isdigit():
            n1 = n1 + version1[i]

    
    for i in range(0, ln2):
        if version2[i] == '0':
            
        if version2[i].isdigit():
            n2 = n2 + version2[i]

    print n1, n2

    n1 = int(n1)
    n2 = int(n2)

    if (n1 > n2):
        return 1
    elif (n1 < n2):
        return -1
    else:
        return 0

if __name__ == '__main__':
    print compareVersion('0.1', '0.05')
    
