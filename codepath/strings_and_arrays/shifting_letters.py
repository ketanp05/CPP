from typing import List

def shift_letters(s: str, shifts:List[int]):
    if not s or not shifts:
        return s
    
    char_list = list(s)

    def shift_char(c, num):
        return chr((ord(c) - ord('a') + num) % 26 + ord('a'))

    cumulative_shift = 0
    for i in range(len(shifts)-1, -1, -1):
        cumulative_shift += shifts[i]
        char_list[i] = shift_char(char_list[i],  cumulative_shift)

    return "".join(char_list)

def main():
    s = "abc"
    shifts = [3,5,9]
    print(shift_letters(s, shifts))

if __name__ == "__main__":
    main()