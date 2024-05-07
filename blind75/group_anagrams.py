from typing import List

class GroupAnagramsProblem:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        pass

def main():
    gap = GroupAnagramsProblem()

    testlist = ['eat', 'hat', 'tah', 'ate', 'tea', 'nat', 'ant', 'pizza']
    print(gap.groupAnagrams(testlist))

if __name__ == "__main__":
    main()