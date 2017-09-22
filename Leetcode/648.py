def replaceWords(l , sentence):

    d = {}

    for word in  l:
        d[word] = len(word)

    words = sentence.split(' ')

    res = ""
    flag = False
    for word in words:
        flag = False
        max_substr_len = 1000
        append_word = ""
        for key in d:
            substr = word[:d[key]]
            if substr in d:
                flag = True
                if d[key] < max_substr_len:
                    max_substr_len = d[key]
                    append_word = substr
                    
            
        if not flag:
            res += word
        else:
            res += append_word
            
        res += " "

    return res[:len(res)-1]
                
if __name__ == '__main__':
    l = ["cat", "bat", "rat"]
    sentence = "a the cattle was rattled by the battery"
    print replaceWords(l, sentence)
