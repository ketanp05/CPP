from typing import List
from collections import defaultdict

class GroupAnagramsProblem:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # if there are no anagram groups then return a dict with list
        # now you cannot have List as your key so later you will see a conversion from a list to a tuple
        result_map = defaultdict(list)

        # i will increment the count at the letters relevant index position to 1
        # for eg: e will have the count 1 at index 4 when the input string has e
        for string_in_strs in strs:
            count = [0] * 26 # 26 letters of an alphabet

            for character in string_in_strs:
                count[ord(character) - ord('a')] += 1

            result_map[tuple(count)].append(string_in_strs)
        
        return result_map.values()

def main():
    gap = GroupAnagramsProblem()

    testlist = ['eat', 'hat', 'tah', 'ate', 'tea', 'nat', 'ant', 'pizza']
    print(gap.groupAnagrams(testlist))

if __name__ == "__main__":
    main()