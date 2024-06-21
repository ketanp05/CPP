from typing import List

def arithmetic_triplets(nums: List[int], diff:int) -> int:
    seen = set()
    counter = 0

    for k in range(len(nums)):
        if (nums[k]-diff) in seen and (nums[k]-2*diff) in seen:
            counter += 1
        seen.add(nums[k])

    return counter

def main():
    nums = [0, 1, 4, 6, 7, 10]
    diff = 3
    print(arithmetic_triplets(nums, diff))

if __name__ == "__main__":
    main()