# cook your dish here
class Solution:
    def containsDuplicate(self, nums:List[int]) -> bool:
        hashset = set()
        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)
        return False
        
def main():
    nums = [1,1,2,3,5]
    print(Solution().containsDuplicate(nums))
    
if __name__ == "__main__":
    main()