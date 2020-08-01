class Solution(object):
    def detectCapitalUse(self, word):
        if word.upper()==word:
            return True
        elif word[0].isupper() and word[1:].islower():
            return True
        elif word.lower()==word:
            return True
        return False
