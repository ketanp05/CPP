from typing import List

class FindMinimum:
    def find_minimum_rotated_sorted_array(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        result = nums[l]

        while l < r:
            # if array is already sorted then the min will be the first element
            if nums[l] < nums[r]:
                result = min(nums[l], result)
                break

            mid = (l+r)//2
            result = min(result, nums[mid])

            if nums[mid] > nums[l]:
                l = mid+1
            else:
                r = mid-1
        
        return result

        

def main():
    fm = FindMinimum()
    # input: [4,5,6,7,0,1,2]
    print(fm.find_minimum_rotated_sorted_array([4,5,6,7,0,1,2]))

if __name__ == "__main__":
    main()