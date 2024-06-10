class Solution:
    def roman_to_int(self, s:str) -> int:
        total = 0
        hashmap = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        for i in range(len(s)):
            if i+1 < len(s) and hashmap[s[i]] < hashmap[s[i+1]]:
                total -= hashmap[s[i]]
            else:
                total += hashmap[s[i]]
        
        return total

def main():
    s = Solution()
    print(s.roman_to_int("MCMXCIV"))

if __name__ == "__main__":
    main()