def longest_common_prefix(strs):
    l = len(strs)
    pre = strs[0]
    i = 1

    while i < l:
        while strs[i].find(pre) != 0:
            pre = pre[:-1]
        i += 1
    return pre


if __name__ == '__main__':
    strs = ["abb", "abc", "abcd", "aefg"]
    print longest_common_prefix(strs)
