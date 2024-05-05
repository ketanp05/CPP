from typing import List

class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        for index_of_nums, number_in_nums in enumerate(nums):
            # logic is : x + y = target, so y = target - x should be in the hashmap
            # if it is then return the index of x and y stored as keys in hashmap
            y = target - number_in_nums
            if y in nums_map:
                return [nums_map[y], index_of_nums]
            nums_map[number_in_nums] = index_of_nums
        return

def main():
    s = Solution()
    print(s.two_sum([2,7,11,15], 26))

if __name__ == "__main__":
    main()