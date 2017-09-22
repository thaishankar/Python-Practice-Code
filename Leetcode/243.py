import sys


def shortestDistance(words, word1 , word2):
    prev = -1
    dist = sys.maxint
    
    for i in range(len(words)):
        if words[i] == word1 or words[i] == word2:
            if prev != -1 and words[prev] != words[i] and (i-prev) < dist:
                dist = i-prev
            prev = i
            
    return dist


"""
def shortestDistance(words, word1, word2):
    p1 = -1
    p2 = -1
    dist = 1000
    for i in range(len(words)):
        if (words[i] == word1):
            p1 = i
        elif (words[i] == word2):
            p2 = i
        if p1 != -1 and p2 != -1 and abs(p1-p2) < dist:
            dist = abs(p1 - p2)
            
    return dist               
"""

if __name__ == '__main__':
    words = ["practice", "makes", "perfect", "coding", "makes"]
    print shortestDistance(words, words[0], words[3])
