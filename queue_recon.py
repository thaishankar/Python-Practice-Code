class Solution(object):
    def reconstructQueue(self, people):
        if not people: return []

        # obtain everyone's info
        # key=height, value=k-value, index in original array
        peopledct, height, res = {}, [], []
        print people
        for i in xrange(len(people)):
            p = people[i]
            if p[0] in peopledct:
                peopledct[p[0]] += (p[1], i),

            else:
                peopledct[p[0]] = [(p[1], i)]
                height += p[0],

        height.sort()      # here are different heights we have
        print height
        print peopledct
        # sort from the tallest group
        for h in height[::-1]:
            peopledct[h].sort()
            print "h = %s %s" %(h, peopledct[h])
            for p in peopledct[h]:
                res.insert(p[0], people[p[1]])

        return res

if __name__ == '__main__':
    people = [[7,1], [4,4], [7,0], [5,0], [6,1], [5,2]]
    s = Solution()
    print s.reconstructQueue(people)
