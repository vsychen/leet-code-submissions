class Solution(object):
    # ALGORITHM: 
    # If there is some substring in words that do not exist in s, return (s needs to contain all substrings of words). If words only have one substring that repeats
    # many times (["a", "a", "a"]), the only word possible for it is a concatenation of all elements ("aaa"), so just check the indexes of this string.
    # Because the question asks for all indexes of the combinations of substrings, it is necessary to check s entirely, instead of checking if each possible word is in s.
    # If s starts with any of the substrings in word, try replacing the start of the substring s' with each of words substrings. If its possible to replace s' with words
    # substrings, it means a combination of words substrings starts in that index. Continue exploring s until all indexes are found.
    def tryString(self, s, words):
        if len(s) == 0: return True
        elif len(list(set(words))) == 1 and len(words) != 1: return ("".join(words)) == s
        else:
            for i in range(len(words)):
                if s.startswith(words[i]):
                    return self.tryString(s[len(words[i]):], words[:i]+words[i+1:])
            return False

    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        try:
            any(s.index(w) for w in words)

            indexes = []
            word_size = len("".join(words))

            if len(list(set(words))) == 1 and len(words) != 1:
                word = "".join(words)
                for i in range(len(s)-word_size+1):
                    if s[i:i+word_size] == word:
                        indexes.append(i)
            else:
                for i in range(len(s)-word_size+1):
                    if any(s[i:].startswith(w) for w in words):
                        if self.tryString(s[i:i+word_size], words):
                            if i not in indexes: indexes.append(i)
                indexes.sort()

            return indexes
        except:
            return []