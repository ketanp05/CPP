from typing import List

class BuySellStock:
    def buy_and_sell_stock(self, prices: List[int]):
        """
        move the left pointer to where the right pointer. right pointer is gonna shift eventually at the end of the loop
        """
        l, r = 0, 1
        max_profit = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_profit = max(profit, max_profit)
            else:
                l = r
            r += 1
        return max_profit

def main():
    bs = BuySellStock()
    prices = [1, 7, 5, 3, 6, 4]
    print(bs.buy_and_sell_stock(prices))

if __name__ == "__main__":
    main()