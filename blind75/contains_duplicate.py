from typing import List

def containsDuplicate(nums:List[int]) -> bool:
    
    # to keep elements that occured once
    checked = set()

    for number in nums:
        # number occured already in the set that means its a duplicate
        if number in checked:
            return True
        checked.add(number)

    return False

def main():
    nums = [1,2,3,4,5,1]
    print(containsDuplicate(nums))

if __name__ == "__main__":
    main()