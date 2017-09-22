import sys

def shortestDistance(words, word1, word2):
    dist = sys.maxint
    prev = -1

    for i in range(len(words)):
        if (words[i] == word1 or words[i] == word2):
            if prev >= 0 and (i - prev) < dist:
                dist = i - prev
            prev = i
            
            
    return dist               

if __name__ == '__main__':
    words = ["practice", "perfect", "perfect", "coding", "makes"]
    print shortestDistance(words, words[0], words[2])
