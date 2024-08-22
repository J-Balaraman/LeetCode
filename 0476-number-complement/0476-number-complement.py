class Solution:
    def findComplement(self, num: int) -> int:
        binary = bin(num)[2:]
        
        reverse = ''.join('1' if x == '0' else '0' for x in binary)

        return int(reverse, 2)
