# 我的解法
class Solution:
    def isValid(self, s: str) -> bool:
        #         采用栈
        chk = []

        for i in range(len(s)):
            if not chk:
                chk.append(s[i])
            elif self.match(chk[-1], s[i]):
                chk.pop()
            else:
                chk.append(s[i])
        return not bool(chk)

    def match(self, s1, s2):
        return (s1 == '(' and s2 == ')') or (s1 == '{' and s2 == '}') or (s1 == '[' and s2 == ']')

# 采用字典映射，如果匹配较多的话
class Solution1:
    def isValid(self, s: str) -> bool:
            stack = []
            mapping = {")": "(", "}": "{", "]": "["}

            for char in s:
                if char in mapping:
                    top_element = stack.pop() if stack else '#'
                    if mapping[char] != top_element:
                        return False
                else:
                    stack.append(char)
            return not stack
if __name__=='__main__':

    a=Solution()

    print(a.isValid("()[]{}"))