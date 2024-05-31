from typing import List

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         indices = list()
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 if(nums[i] + nums[j] == target):
#                     indices.append(i)
#                     indices.append(j)
#         return indices

# def main():
#     obj = Solution()
#     nums = [3,3,3]
#     target = 6
    
#     print(obj.twoSum(nums, target))
    
# if __name__ == "__main__":
#     main()

# optimal


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} #number and index
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[nums[i]] = i;
        return


def main():
    obj = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    
    print(obj.twoSum(nums, target))
    
if __name__ == "__main__":
    main()
