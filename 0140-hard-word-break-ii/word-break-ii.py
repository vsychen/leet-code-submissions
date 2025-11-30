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
    # Construct a Trie to better compare the words in wordDict. Create a dynamic programming array of size len(s). If dp[x] is not empty, it means s[0:x+1]
    # can be constructed with the words in wordDict plus spaces. If it's empty, it cannot. Walk through the dp array. If i==0 or dp[i-1] is not empty, it 
    # means a new word can start at index i. Use a second pointer to check if the next characters make a valid prefix or if it's a valid word. If it's a 
    # valid word, add the combinations of all words in dp[i-1]+" "+new_word to dp[i+j] where j is the size of the new word. If it's a valid prefix, continue 
    # trying. If it's not a valid word, nor a valid prefix, break the small loop and go for the next characters. At the end of the big loop, return the list
    # of sentences in the last position of the array.
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        trie = Trie()

        for w in wordDict:
            trie.insert(w)
        
        dp = [[] for _ in range(len(s))]

        for i in range(len(s)):
            if i == 0 or dp[i-1]:
                w = ""
                for j in range(i, len(s)):
                    w += s[j]
                    if trie.search(w):
                        if j-(len(w)-1) == 0:
                            dp[j].append(w)
                        else:
                            [dp[j].append(t+" "+w) for t in dp[i-1]]
                    elif not trie.isPrefix(w): break

        return dp[-1]

a = Solution()
print(a.wordBreak("catsanddog",["cat","cats","and","sand","dog"]))