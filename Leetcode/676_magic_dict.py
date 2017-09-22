class MagicDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}

    def buildDict(self, words):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """


        for word in words:
            for i in range(len(word)):
                substr = word[:i] + word[i+1:]
                if substr in self.d:
                    self.d[substr] += [(i, word[i])]
                else:
                    self.d[substr] = [(i, word[i])]
       
        

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        for i in range(len(word)):
            substr = word[:i] + word[i+1:]
            if substr in self.d:
                val = self.d[substr]
                for v in val:
                    if v[0] == i and v[1] != word[i]:
                        return True
        return False
        



if __name__ == '__main__':
    m = MagicDictionary()
    words = ["hello", "leetcode"]
    word = "hello"
    m.buildDict(words)
    print m.search(word)
    
