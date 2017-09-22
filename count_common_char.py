
def count_common_char(S):

    d = {}
    for i in range(len(S)):
        curr_d = {}
        for j in range(len(S[i])):
            if S[i][j] not in curr_d:
                d[S[i][j]] += 1
            else:
                d[S[i][j]] += 1

    print d
    common_unique = 0
    for key in d:
        if d[key] == len(S):
             common_unique += 1

    return common_unique

if __name__ == '__main__':
    charSet = ["aghkafgklt", "dfghako", "qwemnaarkf"]
    print count_common_char(charSet)
