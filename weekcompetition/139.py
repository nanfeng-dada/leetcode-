import copy
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        def sdiv(st1,st2):
            s1=copy.deepcopy(st1)
            s2=copy.deepcopy(st2)


            k=0
            rate=len(s1) //len(s2) +1
            while k<=rate:

                if s1[:len(s2)]==s2:
                    k+=1
                    s1=s1[len(s2):]
                else:
                    return k,s1
            return k,0

        while 1:
            k,s=sdiv(str1,str2)
            # if not k:
            #     return ''
            if not s:
                return str2
            else:
                str1,str2=str2,s


a=Solution()
print(a.gcdOfStrings('a','aab'))