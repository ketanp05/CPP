from typing import List

class MostWater:
    def container_with_most_water(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        max_area = 0

        while l < r:
            curr_area = (r - l) * min(height[l], height[r])
            max_area = max(curr_area, max_area)

            if height[l] < height[r]:
                l += 1
            elif height[l] > height[r]:
                r -= 1
            else:
                l += 1
                r -= 1
        
        return max_area

def main():
    mw = MostWater()
    # height = [1,8,6,2,5,4,8,3,7]
    height = [1,1]
    print(mw.container_with_most_water(height))

if __name__ == "__main__":
    main()