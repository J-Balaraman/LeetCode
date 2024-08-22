class Solution:
    def isPalindrome(self, s: str) -> bool:
        palindromeCheck = ''
        lettersOnly = ''
        for char in s:
            if char.isalnum() == True:
                print(char)
                palindromeCheck = char + palindromeCheck
                lettersOnly = lettersOnly + char
        
        lettersOnly = lettersOnly.lower()
        palindromeCheck = palindromeCheck.lower()
        print(lettersOnly, palindromeCheck)
        if lettersOnly == palindromeCheck:
            return True
        else:
            return False
            