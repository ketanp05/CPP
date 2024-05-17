from typing import List

class ThreeSum:
    def three_sum(self, nums: List[int]) -> List[List[int]]:
        """
        a is the elemnet we pick from nums, then for the rest the array we find the pair b,c with two sum two/two pointers approach
        b,c -> through two sum two i.e two pointers approach
        """
        nums.sort()
        result = []
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue
            
            l, r = i+1, len(nums)-1
            while l < r:
                sum_abc = a + nums[l] + nums[r]
                if sum_abc > 0:
                    r -= 1
                elif sum_abc < 0:
                    l += 1
                else:
                    result.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1

        return result

def main():
    ts = ThreeSum()
    nums = [-1,0,1,2,-1,-4]
    print(ts.three_sum(nums))

if __name__ == "__main__":
    main()
