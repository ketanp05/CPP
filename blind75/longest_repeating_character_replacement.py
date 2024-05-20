class LongestRepeatingCharacter:
    def longest_repeating_character(self, s:str, k:int) -> int:
        start, end = 0,0
        max_len = 0
        max_freq = 0
        freq_map = {}

        for end in range(len(s)):
            ch = s[end]
            if ch in freq_map:
                freq_map[ch] += 1
            else:
                freq_map[ch] = 1

            max_freq = max(max_freq, freq_map[ch])

            # see if (window_size - max_freq) exceeds k
            if (end - start + 1 - max_freq) > k:
                freq_map[s[start]] -= 1
                start += 1
            
            max_len = max(max_len, end - start + 1)

        return max_len

def main():
    lr = LongestRepeatingCharacter()
    print(lr.longest_repeating_character("AABABBA", 1))

if __name__ == "__main__":
    main()