class Solution(object):
    # TOPICS: STRING/BACKTRACKING
    # For len(s) less than 4 or with more than 12 characters, there's not a combination possible for IP (13 characters will always have at least one segment with 4 characters,
    # resulting in a value greater than 255). If len(s) is 4, separate all characters with a '.' and return it.
    # Each segment should have at least one character. A segment can have value '0', but can't have anything else starting with zero - '01', for example. The converted 
    # value of a segment should be between '0' (one character) and 255, inclusive (three characters). With these rules in place, walk the string and see all combinations possible. 
    # Use the len(s) constraints to check if there's enough characters remaining for the rest of the validation, or if there's too many characters remaining. In those cases, it's 
    # not necessary to keep checking, as the validation will fail at the end.
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        length = len(s)
        if length < 4 or length > 12: return []
        elif length == 4: return [".".join(list(s))]
        r = []

        def isValid(s):
            if s == '0': return True
            elif s[0] == '0' or int(s) >= 256: return False
            else: return True
        
        for i in range(3):
            if length-1-i <= 9 and isValid(s[:i+1]):
                for j in range(i+1, i+4):
                    if j >= length-2: break
                    elif length-1-j <= 6 and isValid(s[i+1:j+1]):
                        for k in range(j+1, j+4):
                            if k >= length-1: break
                            elif length-1-k <= 3 and isValid(s[j+1:k+1]):
                                if isValid(s[k+1:]):
                                    r.append(".".join([s[:i+1],s[i+1:j+1],s[j+1:k+1],s[k+1:]]))
        
        return r