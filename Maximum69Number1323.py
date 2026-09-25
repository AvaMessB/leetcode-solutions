class Solution:
    def maximum69Number (self, num: int) -> int:
        firstsix = str(num).find('6')
        listnum = list(str(num))
        listnum[firstsix] = '9'
        return int(''.join(listnum))
sol = Solution()
print(sol.maximum69Number(69696969996969))