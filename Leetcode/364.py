"""
def max_depth(arr):
    count = 0
    max_depth = 0
    for i in range(len(arr)):
        if arr[i] == '[':
            count += 1
            if count > max_depth:
                max_depth = count
        elif arr[i] == ']':
            count -= 1
    print "max = %s" % max_depth
    return max_depth

def nested_list_sum(arr):
    s = str(arr)
    depth = max_depth(s) + 1
    res = 0
    for i in range(len(s)):
        if s[i].isdigit():
           res += depth * int(s[i])
        elif s[i] == '[':
            depth -= 1
        elif s[i] == ']':
            depth += 1
        else:
            continue
            
    return res
"""

def depthSum(nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        def depthSumHelper(nestedList, depth):
            res = 0
            for l in nestedList:
                if l.isdigit():
                    res += l.getInteger() * depth
                else:
                    res += depthSumHelper(l.getList(), depth + 1)
            return res
        return depthSumHelper(nestedList, 1)

if __name__ == '__main__':
    arr = [1, [1, [2]]]
    print depthSum(arr)
