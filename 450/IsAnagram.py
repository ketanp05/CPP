class Solution:
    def isAnagram(self, s:str, t:str) -> bool:
        if len(s) != len(t):
            return False
        
        CountS, CountT = {}, {}
        
        for letter_s in s:
            CountS[letter_s] = 1 + CountS.get(letter_s, 0)
        
        for letter_t in t:
            CountT[letter_t] = 1 + CountT.get(letter_t, 0)
            
        for key in CountS:
            if CountS[key] != CountT.get(key, 0):
                return False
        return True
        
        # if(len(s) != len(t)):
        #     return False
        # count = 0
        # for i in range(len(s)):
        #     if t[i] in s:
        #         count += 1
    
        # if count == len(s):            
        #     return True
    
    # def isAnagram(self, s:str, t:str) -> bool:
    #     return sorted(s) == sorted(t)
    
    # def isAnagram(self, s:str, t:str) -> bool:
    #     return Counter(s) == Counter(t)
        

def main():
    s = "aacc"
    t = "ccac"
    obj = Solution()
    print(obj.isAnagram(s, t))
    
if __name__ == "__main__":
    main()

# optimal

