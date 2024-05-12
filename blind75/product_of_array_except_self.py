from typing import List

class ProductExceptSelf:
    def product_except_self(self, nums: List[int]) -> List[int]:
        """
        Computes an array with each index having value which is the product of all the other values except itself
        
        Args:
        nums[List]: input array

        Returns:
        result[List]: resultant array
        """
        n = len(nums)
        res = [1] * n

        # update res with valid prefixes for nums[i]
        for i in range(1, n):
            res[i] = res[i-1] * nums[i-1]

        # on the fly multiply postfix with res
        suffix_product = 1
        for j in range(n-1, -1, -1):
            res[j] = res[j] * suffix_product
            suffix_product *= nums[j]

        return res


def main():
    pes = ProductExceptSelf()
    print(pes.product_except_self([1,2,3,4]))
    print(pes.product_except_self([-1,1,0,-3,3]))

if __name__ == "__main__":
    main()