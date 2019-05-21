class Solution:
    def titleToNumber(self, s: str) -> int:
        ls=[ord(x) for x in list(s)][::-1]
        num=0
        while ls:
            num=num*26+ls.pop()-ord('A')+1
        return num