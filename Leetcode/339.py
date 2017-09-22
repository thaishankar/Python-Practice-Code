"""
def nested_list_sum(arr):
    s = str(arr)
    depth = 0
    res = 0
    for i in range(len(s)):
        if s[i].isdigit():
           res += depth * int(s[i])
        elif s[i] == '[':
            depth += 1
        elif s[i] == ']':
            depth -= 1
        else:
            continue
            
    return res
"""

def nested_list_sum(arr, depth):
    res = 0
    for i in arr:
        if i.isInteger():
           res += depth * i
        else:
            nested_list_sum(arr[i], depth+1)
            

    return res

if __name__ == '__main__':
    arr = [1, [1, [2]]]
    print nested_list_sum(arr, 1)
