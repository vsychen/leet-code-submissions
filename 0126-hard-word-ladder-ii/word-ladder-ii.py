class Solution(object):
    # TOPICS: STRING/BACKTRACKING/BFS
    # If endWord not in wordList, it's impossible to get from beginWord to endWord. Put beginWord in the list of 'strings to be checked' and create a 
    # dictionary of 'parent strings'. While there are strings to be checked and endWord is not in this list (endWord is still not found), create a new
    # list of 'words that were visited in this round'. At each 'round', search inside wordList for words that are 1 character away from the words to
    # be checked. Save them as the 'next layer/round strings' and also get track of their parents (i.e. which words can derivate them when changing only
    # one character). After getting all words of a layer/round, and their parents, remove them from the wordList to avoid infinite looping. Update the
    # 'strings to be checked' list with the 'next layer/round strings' and repeat until endWord is found.
    # After getting the useful words and its parents until endWord, reconstruct all paths from endWord to beginWord and return it as the answer.
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        if endWord not in wordList: return []

        def diff(s1, s2):
            return len([1 for i in range(len(s1)) if s1[i] != s2[i]])

        toCheck = [beginWord]
        parents = {}

        while toCheck and endWord not in toCheck:
            nextLayer = []

            for bw in toCheck:
                for nw in wordList:
                    if diff(bw,nw) == 1:
                        if nw not in nextLayer: nextLayer.append(nw)

                        if nw not in parents:
                            parents[nw] = [bw]
                        else:
                            parents[nw].append(bw)
                nextLayer.extend([nw for nw in wordList if diff(bw,nw) == 1 and nw not in nextLayer])
            
            for w in nextLayer:
                wordList.remove(w)
            
            toCheck = nextLayer
        
        answer = []

        def reconstruct(beginWord, endWord):
            if endWord not in parents: return []
            aux = parents[endWord]
            print(aux, endWord)
            if beginWord in aux:
                return [[beginWord, endWord]]
            else:
                r = []
                for p in aux:
                    prev = reconstruct(beginWord, p)
                    for e in prev:
                        e.extend([endWord])
                        r.append(e)
                return r

        return reconstruct(beginWord, endWord)