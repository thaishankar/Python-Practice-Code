def count_substr(s, l):

    d = {}
    for i in range(len(s) - 2):
        sub = s[i: i+l]
        if sub in d:
            d[sub] += 1
        else:
            d[sub] = 1

    for key in d:
        print key, d[key]
    


if __name__ == '__main__':
    s = "ABCGRETCABCG"
    l = 3
    print count_substr(s, l)
