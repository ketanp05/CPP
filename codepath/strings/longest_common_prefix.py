from typing import List

def longest_common_prefix(strs: List[str]) -> str:
    # test cases
    result = ""

    # sorting so that the string with the least length comes in case they do have longest common prefix
    # strs.sort() # O(nlogn)
    for i in range(len(strs[0])): # O(m)
        for s in strs: # O(n)
            # handling the edge case right away
            # s[i] might go out of bounds if the strs array has strings less than len(strs[0])
            # adding the condition to stop and return : i == len(s)
            if i == len(s) or s[i] != strs[0][i]:
                return result
        result += strs[0][i]

    return result

def main():
    # strs = ["dad", "mom", "bro"]
    # strs = ["flower", "flow", "flowering"]
    # strs = ["flower", "flow", "flight"]
    print(longest_common_prefix(strs))

if __name__ == "__main__":
    main()

"""
I wouldnt say the below solution is more optimized but it uses python's
inbuilt 'startswith' to check if a string starts with a 'char' or 'string'
passed inside startswith
"""

# from typing import List

# def longest_common_prefix(strs: List[str]) -> str:
#     prefix = strs[0]

#     for s in strs[1:]:
#         while not s.startswith(prefix):
#             prefix = prefix[:-1]
            
#             # if prefix becomes empty that is no prefix was found
#             if not prefix:
#                 return ""
    
#     return prefix

# def main():
#     # strs = ["dad", "mom", "bro"]
#     # strs = ["flower", "flow", "flowering"]
#     strs = ["flower", "flow", "flight"]
#     print(longest_common_prefix(strs))

# if __name__ == "__main__":
#     main()