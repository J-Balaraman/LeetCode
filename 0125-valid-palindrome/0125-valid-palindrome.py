class Solution:
    def isPalindrome(self, s: str) -> bool:
        palindromeCheck = ''
        lettersOnly = ''
        for char in s:
            if char.isalnum() == True:
                palindromeCheck = char + palindromeCheck
                lettersOnly = lettersOnly + char
        
        lettersOnly = lettersOnly.lower()
        palindromeCheck = palindromeCheck.lower()
        if lettersOnly == palindromeCheck:
            return True
        else:
            return False
            