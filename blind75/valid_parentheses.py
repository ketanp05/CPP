class ValidParentheses:
    # # stack helper functions
    # def __init__(self):
    #     self.stack = []
    
    # def is_empty(self):
    #     if len(self.stack) == 0:
    #         return True
    #     else:
    #         return False

    # def push(self, item):
    #     self.stack.append(item)
    
    # def peek(self):
    #     if not self.is_empty():
    #         return self.stack[-1]
    #     return None    
    
    # def size(self):
    #     return len(self.stack)
    
    # def pop(self):
    #     if not self.is_empty():
    #         return self.stack.pop()
    #     return None

    # def isValid(self, s: str) -> bool:
    #     hashmap = {
    #         ")":"(",
    #         "}":"{",
    #         "]":"["
    #     }
    #     for ch in s:
    #         if (ch in hashmap) and (self.peek() == hashmap[ch]) and (not self.is_empty()):
    #             self.pop()
    #         else:
    #             self.push(ch)

    #     if self.is_empty():
    #         return True
    #     else:
    #         return False

    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {
            ")":"(",
            "}":"{",
            "]":"["
        }
        for ch in s:
            if ch in hashmap:
                if (stack[-1] == hashmap[ch]) and stack:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)

        return True if not stack else False
        
def main():
    vp = ValidParentheses()
    print(vp.isValid("{()[]}"))

if __name__ == "__main__":
    main()