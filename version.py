def compareVersion(v1, v2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        
        n1 = 0
        n2 = 0
        ln1 = len(v1)
        ln2 = len(v2)
        i = 0
        j = 0
        while(i<ln1 or j<ln2):
     
            while(i<ln1 and v1[i] != '.'):
                n1 = n1*10 + int(v1[i])
                i += 1
            
            while(j<ln2 and v2[j] != '.'):
                n2 = n2*10 + int(v2[j])
                j += 1
            
          
            if (n1<n2):
                return -1
            elif (n1>n2):
                return 1
            
            n1 = 0
            n2 = 0
            i += 1
            j += 1
        return 0
    

if __name__ == '__main__':
    v1 = "1.1"
    v2 = "1.1.11"
    print compareVersion(v1, v2)
