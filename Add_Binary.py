class Solution:
    def addBinary(self, a: str, b: str) -> str:
        pass
sum = ''
a = '0'
b = '0'
carry = 0
s = int(a) + int(b) + carry

if s == 0:
    sum = sum + '0'
    carry = 0
elif s == 1:
    sum = sum + '1'
    carry = 0
elif s == 2:
    sum = sum + ''
print(sum)
