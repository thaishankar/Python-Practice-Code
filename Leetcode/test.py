def shortest_word_distance(words, word1, word2):

    prev = -1
    min_dist = 1000

    for i in range(len(words)):
        if words[i] == word1 or words[i] == word2:
            if prev == -1:
                prev = i
            else:
                if i - prev < min_dist:
                    min_dist = i - prev
                prev = i
    return min_dist

if __name__ == '__main__':
    words = ["practice", "makes", "perfect", "coding", "makes"]
    word1 = "makes"
    word2 = "coding"
    print shortest_word_distance(words, word1, word2)
