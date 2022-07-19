import re

def palindrome(string: str):
    pattern = r'[^A-Za-z0-9]+'
    string = re.sub(pattern, '', string.lower())

    i = 0
    j = len(string)-1
    while i < j:
        print("i have fun now")
        if string[i] != string[j]:
            return False
     
        i += 1
        j -= 1
    return True

palindrome("A man, a plan, a canal: Panama")

#after lots and lots of googling and reading I believe my function has the time complexity of O(n)
# what solidifies that belief is that my function is linear and grows with the input.