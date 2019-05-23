# 两个哈希表解决相互对应地问题
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic = {}
        dic2 = {}
        l = len(s)
        for i in range(l):
            if s[i] in dic:
                if dic[s[i]] != t[i]:
                    return False
            else:
                dic[s[i]] = t[i]
            if t[i] in dic2:
                if dic2[t[i]] != s[i]:
                    return False
            else:
                dic2[t[i]] = s[i]

        return True
# 一个哈希表映射，把哈希表中的values取出来
class Solution1:
    def isIsomorphic(self, s: str, t: str) -> bool:
        res={}
        if len(s)!=len(t):
            return False
        else:
            for i in range(len(s)):
                if s[i] in res:
                    if res[s[i]]!=t[i]:
                        return False
                else:
                    if t[i] in res.values():
                        return False
                res[s[i]]=t[i]
        return True
class Solution2:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return [*map(s.index, s)] == [*map(t.index, t)]
    # 这句话相当于生成保存每个字符索引值的列表，同样的字符会取第一个出现的索引，因此，
    # 求解了相同位置的字符相同的问题
    # [s.index(x) for x in s]==[t.index(x) for x in t]