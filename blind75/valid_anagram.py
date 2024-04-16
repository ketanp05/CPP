from collections import Counter
from typing import List

def isAnagram(s: str, t: str) -> bool:
    # logic 1: flawed, does not take into account freuqency of letters in the string
    # if len(s) == len(t):
    #     for letter in s:
    #         if letter not in t:
    #             return False
    # return True

    # logic 2: flawed, does not take into account freuqency of letters in the string
    # set_s = set(list(s))
    # set_t = set(list(t))

    # if len(s) == len(t):
    #     if set_s == set_t:
    #         return True
    #     else:
    #         return False

    # return False

    # logic 3: using the logic of frequency
    # if len(s) != len(t):
    #     return False

    # count_of_s = {}
    # count_of_t = {}

    # for index in range(len(s)):
    #     count_of_s[s[index]] = count_of_s.get(s[index], 0) + 1
    #     count_of_t[t[index]] = count_of_t.get(t[index], 0) + 1

    # return count_of_s == count_of_t

    # logic 4: using counter inbuilt collections method
    if Counter(s) == Counter(t):
        return True
    return False

def main():
    isAnagram("anagram", "nagaram")

if __name__ == "__main__":
    main()