class Wildcard:
    def __eq__(self, anything):
        return True

class Solution(object):
    # TOPICS: STRING/GREEDY
    # First step is to simplify the pattern; if there's double wildcard characters, it's possible to reduce the pattern (** is the same as *). The base cases are when the string or
    # the pattern are empty. If both are empty, they match. If only the string is empty, double check the pattern to see if the remaining characters are *s. If only the pattern is
    # empty, they don't match. If the pattern has only one character, *, whatever the string is, it matches. Next, "trim" the start and end of both string and pattern, matching 
    # the start and end of them. The result will be a string, and a pattern that starts and ends with *. At this point, it is possible to split the pattern using * as the separator
    # and check if each of the substrings exists in the string. In case of multiple appearances, it is necessary to consider all of them. In the example ("abcabczzzde", "*abc???de*")
    # if the first "abc" is matched with the pattern, the answer will be False. The pattern should match the first "abc" with the "*" and the second "abc" with the pattern "abc" to 
    # return True.
    # Shout out to this Stack Overflow answer (https://stackoverflow.com/a/69217591) that showed me how to create a Wildcard character for comparison and this answer 
    # (https://stackoverflow.com/a/17870684) showing how to find the index of a sublist inside a list.
    def simplify(self, p):
        lst = list(p)
        i = 1
        while i < len(lst):
            if lst[i-1] == "*" and lst[i] == "*":
                lst.pop(i)
            else:
                i += 1
        return "".join(lst)
    
    def getIndex(self, s, p):
        try:
            if "?" not in p:
                return s.index(p)
            else:
                s_lst = list(s)
                p_lst = [(x if x != "?" else Wildcard()) for x in list(p)]

                for i in (i for i,e in enumerate(s_lst) if e==p_lst[0]):
                    if s_lst[i:i+len(p_lst)] == p_lst:
                        return i
                return -1
        except:
            return -1
    
    def searchTokens(self, s, t):
        for i in range(len(t)):
            if not s and t: return False

            index = self.getIndex(s, t[i])
            if index == -1: return False
            else: s = s[index+len(t[i]):]
        return True

    def matchTokens(self, s, p):
        if not s and not p: return True
        elif not s and p: return [t for t in p if t != "*"] == []
        elif s and not p: return False

        if len(p) == 1:
            t = p[0]
            if t == "*": return True
            elif t == "?": return len(s) == 1
            else: return len(s) == 1 and s[0] == t
        else:
            while p[0] != "*":
                if s[0] == p[0] or p[0] == "?":
                    s = s[1:]
                    p = p[1:]
                else:
                    return False
                
                if not s and not p: return True
                elif not s: return [t for t in p if t != "*"] == []
                elif not p: return False
            
            while p[-1] != "*":
                if s[-1] == p[-1] or p[-1] == "?":
                    s = s[:-1]
                    p = p[:-1]
                else:
                    return False

                if not s and not p: return True
                elif not s: return [t for t in p if t != "*"] == []
                elif not p: return False
            
            lst = [x for x in p.split("*") if x != ""]
            l = len("".join(lst))

            if len(s) < l: return False

            for i in range(len(s) - l + 1):
                if self.searchTokens(s[i:], lst):
                    return True
        return False

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        return self.matchTokens(s, self.simplify(list(p)))