class Solution:
    def integer_replacement(self, n: int) -> int:
        def replacement(n, count) -> int:
            # base case
            if n == 1:
                return count
            
            # even or odd check
            if n%2 == 0:
                return replacement(n//2, count + 1)
            else:
                return min(replacement(n-1, count+1), replacement(n+1, count+1))
            
        count = 0
        return replacement(n , count)

def main():
    s = Solution()
    n = 7
    print(s.integer_replacement(n))

if __name__ == "__main__":
    main()