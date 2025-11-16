class Solution(object):
    # TOPICS: STRING/DYNAMIC PROGRAMMING/BACKTRACKING
    # Walk through the word checking if the substring until the character x is a palindrome. For any palindrome found, test the rest of the string for palindromes.
    # There will always be at least a basic palindrome of a character only. When all of the string is checked, return the palindromes to the previous call and 
    # combine the palindromes found with the previous palindromes until you have the list of all palindromes possible. Return this list of lists of strings as
    # the answer.
    # For the palindrome checking, if the word is one character long, it's a palindrome. For anything bigger than 1 character, divide the word in the middle and
    # check the first substring with the second substring reversed. If the length of the string is odd, do not consider the middle character for the checking (i.e.
    # the first substring is anything before the middle character and the second substring is anything after the middle character). If the length of the string is
    # even, the middle character will be part of the second substring (i.e. the first substring is anything before the middle character and the second substring is
    # anything from the middle character onwards).
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if len(s) == 0: return []
        elif len(s) == 1: return [[s]]

        def checkWord(word):
            answer = []

            for i in range(1, len(word)+1):
                if word[:i] == word[:i][::-1]:
                    if word[i:]:
                        aux = checkWord(word[i:])
                        answer.extend([[word[:i]]+a for a in aux])
                    else:
                        answer.append([word[:i]])
            return answer

        return checkWord(s)