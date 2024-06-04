# a simple memoization example.
# problem: fibonaci numbers

def fibonaci_memo(n, memo={}):
    # caching: we return the result if its already computed/calculated
    if n in memo:
        return memo[n]
    # the general base case for numbers less than 1 and including
    if n <= 1:
        return n

    # lets cache our results
    memo[n] = fibonaci_memo(n-1, memo) + fibonaci_memo(n-2, memo)

    return memo[n]

def main():
    print(fibonaci_memo(10))

if __name__ == "__main__":
    main()