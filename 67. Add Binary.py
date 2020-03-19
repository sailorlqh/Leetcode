class Solution:
    def addBinary(self, a: str, b: str) -> str:
        temp1 = int(a, 2)
        return '{0:b}'.format(int(a, 2) + int(b, 2))