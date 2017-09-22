def shortestDistance(words, word1, word2):
    p1 = -1
    p2 = -1
    dist = 1000
    for i in range(len(words)):
        if (words[i] == word1):
            p1 = i
        if (words[i] == word2):
            p2 = i
        if p1 != -1 and p2 != -1 and abs(p1-p2) < dist:
            dist = abs(p1 - p2)
            
    return dist               

if __name__ == '__main__':
    words = ["practice", "makes", "perfect", "coding", "makes"]
    print shortestDistance(words, words[1], words[3])
