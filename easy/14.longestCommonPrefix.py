# 该最长子串问题，比较的起始位相同，为简化版本
# 我的解法
class Solution:
    def longestCommonPrefix(self, strs: list) -> str:

        num = len(strs)
        if num == 0:
            return ''
        l = min([len(x) for x in strs])
        if l == 0:
            return ''
        for i in range(l ):
            for j in range(num - 1):
                if strs[j][i] != strs[j + 1][i]:
                    return strs[j][:i]
        return strs[0][:l]
# 网友解法
# python两种让你拍大腿的解法，时间复杂度你想象不到，短小精悍。
# 1、利用python的max()和min()，在Python里字符串是可以比较的，按照ascII值排，举例abb， aba，abac，最大为abb，最小为aba。
# 所以只需要比较最大最小的公共前缀就是整个数组的公共前缀
class Solution1:
    def longestCommonPrefix(self, strs):
        if not strs: return ""
        s1 = min(strs)
        s2 = max(strs)
        for i,x in enumerate(s1):
            if x != s2[i]:
                return s2[:i]
        return s1

class Solution2:
    def longestCommonPrefix(self, strs):
        if not strs: return ""
        ss = list(map(set, zip(*strs)))
        res = ""
        for i, x in enumerate(ss):
            x = list(x)
            if len(x) > 1:
                break
            res = res + x[0]
        return res

# 反向减少
class Solution3:
    def longestCommonPrefix(self, strs: list[str]) -> str:

        if len(strs) < 1:
            return ""

        ret = strs[0][:len(min(strs))]

        for i in range(1, len(strs)):
            while ret != strs[i][:len(ret)]:
                ret = ret[:len(ret) - 1]
                if not ret:
                    return ""

        return ret
# 本题可采用分治法,但对于时间复杂度没有改善
if __name__=='__main__':

    a=Solution2()

    print(a.longestCommonPrefix(["flower","flow","flight"]))