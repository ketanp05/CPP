from collections import defaultdict

class Solution:
    def character_replacement(self, s: str, k: int) -> int:
        if not s and k == 0:
            return 0
        
        left = 0
        max_count = 0
        max_len = 0
        count = defaultdict(int)

        for right in range(len(s)):
            count[s[right]] += 1
            max_count = max(max_count, count[s[right]])

            # if frequency of non repeating characters exceed k
            # window size - maxcount > k
            if ((right - left + 1) - max_count) > k:
                count[s[left]] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len

def main():
    s = Solution()
    print(s.character_replacement("AAAA", k = 0))

if __name__ == "__main__":
    main()