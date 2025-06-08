class Solution(object):
    # TOPICS: STRING
    # Generate a tree where each path is either add "(" or ")". Do not proceed with paths with more ")" than "(", as they are not valid parenthesis 
    # combinations. When both the number of "(" and ")" are equal to n, the string is a valid parenthesis combination.
    # Obs: The question restrictions specify that max(n) = 8, so another approach is just hard code all answers from n = 1 to n = 8.
    def getTree(self, substr, open, close, n):
        if open == n and close == n: return [substr]
        elif open+close < n<<1:
            r = []
            r.extend(self.getTree(substr+"(", open+1, close, n))
            if open > close:
                r.extend(self.getTree(substr+")", open, close+1, n))
            return r
        else: return []

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0: return []
        return self.getTree("(", 1, 0, n)