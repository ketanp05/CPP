from typing import List

class DecodeString:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] != ']':
                stack.append(s[i])
            else:
                substring = ""
                while stack[-1] != "[":
                    substring = stack.pop() + substring
                stack.pop()

                digit = ""
                while stack and stack[-1].isdigit():
                    digit = stack.pop() + digit
                
                stack.append(int(digit) * substring)
        
        return "".join(stack)

def main():
    ds = DecodeString()
    print(ds.decodeString("3[a2[c]]"))
    print(ds.decodeString("3[a]2[bc]"))
    print(ds.decodeString("2[abc]3[cd]ef"))

if __name__ == "__main__":
    main()