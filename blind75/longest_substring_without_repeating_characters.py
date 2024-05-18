class LongestSubstring:
    def longest_substring(self, s: str) -> int:
        start, end = 0, 0
        max_len = 0
        hashmap = {}

        for end in range(len(s)):
            if s[end] in hashmap and hashmap[s[end]] >= start:
                start = hashmap[s[end]] + 1

            hashmap[s[end]] = end

            # size of the substrig is 'end - start + 1'
            max_len = max(max_len, end - start + 1)

        return max_len
        

def main():
    ls = LongestSubstring()
    print(ls.longest_substring("abcabcabcbb"))

if __name__ == "__main__":
    main()