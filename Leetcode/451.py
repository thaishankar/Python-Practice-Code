import operator
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        char_list = {}
        for char in s:
            if char in char_list:
                char_list[char] += 1
            else:
                char_list[char] = 1

        l = [(v, k) for k, v in char_list.items()]
        l.sort()
        l.reverse()

        s = ""
        for val in l:
            s+= val[1] * val[0]

        print s


if __name__ == '__main__':
    s = Solution()
    string = "tree"
    s.frequencySort(string)
