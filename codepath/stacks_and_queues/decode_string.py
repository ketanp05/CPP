class Solution:
    def decodeString(self, s: str) -> str:
        string_stack = []
        for i in range(len(s)):
            if s[i] != ']':
                string_stack.append(s[i])
            else:
                result = ""
                while string_stack[-1] != '[':
                    result = string_stack.pop() + result # pop char and append to result
                string_stack.pop() # pop '['

                num = ""
                while string_stack and string_stack[-1].isdigit():
                    num = string_stack.pop() + num

                string_stack.append(int(num)*result)
        
        return "".join(string_stack)
    
def main():
    ds = Solution()
    print(ds.decodeString("3[a2[c]]"))
    print(ds.decodeString("3[a]2[bc]"))
    print(ds.decodeString("2[abc]3[cd]ef"))

if __name__ == "__main__":
    main()