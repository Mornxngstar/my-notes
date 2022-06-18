
def is_palindrome(word):
    assert len(word) > 0, "Not empty text please."
    return word == word[::-1]

print(is_palindrome(""))