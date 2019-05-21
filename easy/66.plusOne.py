# 相当pythonic的解答，误用
class Solution:
    def plusOne(self, digits: list) -> list:
        return [int(i) for i in str(int(''.join(str(x) for x in digits))+1)]

class Solution1:
    def plusOne(self, digits: list) -> list:
        n = len(digits)
        for i in range(n-1,-1,-1):
            digits[i]+=1
            if digits[i]==10:
                digits[i] = 0
            else:
                break
        if digits[0]==0:
            return [1]+digits
        else:
            return digits

# 非语言限制解法
class Solution2:
    def plusOne(self, digits: list) -> list:
        num=0
        l=len(digits)
        for i in range(l):
            num=num*10+digits[i]
        num+=1
        lst=[]
        while num:
            lst=[num%10]+lst
            num=num//10
        return lst


if __name__=='__main__':

    a=Solution2()

    print(a.plusOne([9,9,9,9]))
