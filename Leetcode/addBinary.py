class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        
        digit_a = list(a)
        digit_b = list(b)
        la = len(digit_a)
        lb = len(digit_b)
        carry = 0
        res = []
        
        if la > lb:
            for i in range(0, la-lb):
                digit_b.insert(0, '0')
            lb = la
        elif lb > la:
            for i in range(0, lb-la):
                digit_a.insert(0, '0')
            la = lb
            
        
        for i in range(lb-1, -1, -1):
            print digit_a[i], digit_b[i]
            sum1 = int(digit_a[i]) ^ int(digit_b[i]) ^ carry
            res.insert(0, str(sum1))
            print res
            print sum1, carry
            carry = int(digit_a[i]) & int(digit_b[i]) | int(digit_a[i]) & carry | int(digit_b[i]) & carry
            
        if carry:
            res.insert(0, '1')
            
        return ''.join(res)


if __name__ == '__main__':
    S = Solution()
    print S.addBinary("11", "11")
