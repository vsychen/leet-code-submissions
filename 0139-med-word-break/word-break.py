class TrieNode(object):
    def __init__(self):
        self.children = [None]*26
        self.isEndOfWord = False

class Trie(object):
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        curr = self.root

        for c in word:
            index = ord(c)-ord('a')
            if not curr.children[index]:
                curr.children[index] = TrieNode()
            curr = curr.children[index]

        curr.isEndOfWord = True
    
    def search(self, word):
        curr = self.root

        for c in word:
            index = ord(c)-ord('a')
            if not curr.children[index]:
                return False
            curr = curr.children[index]

        return curr.isEndOfWord

    def isPrefix(self, word):
        curr = self.root
        
        for c in word:
            index = ord(c)-ord('a')
            if not curr.children[index]:
                return False
            curr = curr.children[index]
        
        return True

class Solution(object):
    # TOPICS: ARRAY/STRING/DYNAMIC PROGRAMMING/TRIE
    # Construct a Trie to better compare the words in wordDict. Create a dynamic programming array of size len(s). If dp[x] is 1, it means dp[0:x+1] can be
    # constructed with the words in wordDict. If it's 0, it cannot. Walk through the dp array. If i==0 or dp[i-1]==1, it means i is in position to start a
    # new word. Starting from i, use a second pointer to check if the next characters make a valid prefix or if it's a valid word. If it's a valid word, 
    # mark on the dp array as 1. If it's a valid prefix, continue trying. If it's not a valid word, nor a valid prefix, break the small loop and go for the
    # next characters. At the end of the big loop, if the last position of the dp array is 1, the word can be constructed with wordDict. If it's not, it
    # cannot.
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if len(s) == 0 or s in wordDict: return True

        trie = Trie()

        for w in wordDict:
            trie.insert(w)
        
        dp = [0]*len(s)

        for i in range(len(s)):
            if i == 0 or dp[i-1] == 1:
                w = ""
                for j in range(i, len(s)):
                    w += s[j]
                    if trie.search(w): dp[j] = 1
                    elif not trie.isPrefix(w): break

        return dp[-1] == 1