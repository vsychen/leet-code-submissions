class Solution(object):
    # TOPICS: STRING/BFS
    # If endWord not in wordList, it's impossible to get from beginWord to endWord. Change the wordList to a wordSet for efficient reading. For each 
    # iteration, generate all 'one character away' words from the current words and check if they are inside the wordSet. If they are, put them in the
    # next round of generating words. Remove these words from the set to avoid infinite looping. For each iteration, increase the count by one. Repeat
    # these steps until the endWord is found or until toCheck is empty (if the endWord cannot be reached, there will be a moment when toCheck will
    # become empty). If there's anything in toCheck at the end of the iterations, return the counter+1. If toCheck is empty, return 0.
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        if endWord not in wordList: return 0
        lowercase = 'abcdefghijklmnopqrstuvwxyz'

        def generate_words(s1):
            words = []
            for i in range(len(s1)):
                words.extend([s1[:i] + lowercase[j] + s1[i+1:] for j in range(26)])
            return words

        toCheck = set([beginWord])
        wordSet = set(wordList)
        count = 0

        while toCheck and endWord not in toCheck:
            words = set([])
            count += 1
            for bw in toCheck:
                [words.add(w) for w in generate_words(bw) if w in wordSet]
            wordSet.difference_update(words)
            toCheck = words
        
        if endWord in toCheck:
            return count + 1
        else:
            return 0