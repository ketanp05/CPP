# def substring_match(s1: str, s2: str) -> bool:
#     # test cases
#     # happy case
#     # input: s1: "laboratory", s2: "rat" // output: True
    
#     # edge case
#     # input: s1: "catgod", s2:""
#     if s2 == "":
#         return True
#     if s1 == s2:
#         return False
    
#     j, s2_len, match = 0, 0, 0

#     for i in range(len(s1)):
#         if s1[i] == s2[0]:
#             k = i
#             while j < len(s2):
#                 if s1[k] == s2[s2_len]:
#                     match += 1
#                     s2_len += 1
#                     k += 1
#                 j += 1

#     return True if match == len(s2) else False

# def main():
#     s1 = "laboratory"
#     s2 = "rat"
#     print(substring_match(s1, s2))

# if __name__ == "__main__":
#     main()


# optimized approach
def substring_match(s1: str, s2: str) -> bool:
    if s2 == "":
        return True  # An empty substring is always found.
    if s1 == s2:
        return True  # If both strings are identical.
    
    len_s1 = len(s1)
    len_s2 = len(s2)
    
    # Iterate through each character in s1
    for i in range(len_s1 - len_s2 + 1):
        # Check if the substring starting at i matches s2
        match = True
        for j in range(len_s2):
            if s1[i + j] != s2[j]:
                match = False
                break
        if match:
            return True  # Found a match
    
    return False  # No match found

def main():
    s1 = "laboratory"
    s2 = "rat"
    print(substring_match(s1, s2))  # Output: True

    s1 = "catgod"
    s2 = ""
    print(substring_match(s1, s2))  # Output: True

    s1 = "hello"
    s2 = "ll"
    print(substring_match(s1, s2))  # Output: True

    s1 = "hello"
    s2 = "world"
    print(substring_match(s1, s2))  # Output: False

if __name__ == "__main__":
    main()
