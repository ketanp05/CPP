from typing import List

class Solution:
    def letter_combination(self, digits: str) -> List[str]:
        hashmap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        # test cases
        # happy / initial test cases
        if not digits or digits == 1 or digits == 0:
            return []
        
        result = [] # list to store our combinations
        # recusrive solution
        def helper(combination, index):
            # base case
            if index == len(digits):
                result.append(combination)
                return
            
            # recursive
            for c in hashmap[digits[index]]:
                helper(combination + c, index+1)

        helper("", 0)

        return result


def main():
    s = Solution()
    # digits = "23"
    # digits = ""
    digits = "334"
    print(s.letter_combination(digits))

if __name__ == "__main__":
    main()