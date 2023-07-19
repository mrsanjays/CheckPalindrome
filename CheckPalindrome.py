def CheckPalindrome(String,l,r):
    if len(String)==0: return 0
    if len(String)<=2:
        return 1
    if l>r:
        return 1
    if String[l]!=String[r]:
        return 0
    return CheckPalindrome(String,l+1,r-1)

if __name__ == '__main__':
    String=input()
    print(CheckPalindrome(String,0,len(String)-1))
"""
Write a recursive function that checks whether string A is a palindrome or Not.
Return 1 if the string A is a palindrome, else return 0.

Note: A palindrome is a string that's the same when read forward and backward.
"""