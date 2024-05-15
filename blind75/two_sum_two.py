from typing import List

class TwoSumTwo:
    def two_sum_two(self, nums: List[int], target: int) -> List[int]:
        """
        Using the two pointer approach

        Args:
        target (int): target value
        nums (List[int]): input list of numbers

        Returns:
        List[int] : list of indices
        """
        
        nums = sorted(nums)
        i, j = 0, len(nums)-1
        k = 0
        while k < len(nums):
            if nums[i] + nums[j] == target:
                return [i+1, j+1]
            elif nums[i] + nums[j] > target:
                j -= 1
                k += 1
            else:
                i += 1
                k += 1
        return

def main():
    tst = TwoSumTwo()
    print(tst.two_sum_two([2,7,11,15], 9))

if __name__ == "__main__":
    main()