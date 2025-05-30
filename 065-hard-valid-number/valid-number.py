class Solution(object):
    # TOPICS: STRING
    # First, change each character from input to the corresponding token. A character can be a "dot", a "signal", a "try-exponent" (an "e"), a "letter" (any letter excluding "e"), or
    # a number. If there's any "letter" in the string, return False. If there's signals, for each "signal" check the following tokens and replace any of the valid sublists to the
    # corresponding term. After checking for signals, check for digits. After the digits, if there's any digits left, they are integers. Finally, check the tokens for exponents.
    # At the end of the checking, there will be only one number remaining. If there's anything that is not a "integer", "decimal" or "exponent", the string is not valid. Otherwise, it
    # is valid.
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s: return False

        tokens = []
        for i in range(len(s)):
            if s[i] == ".": tokens.append("dot")
            elif s[i] == "+" or s[i] == "-": tokens.append("signal")
            elif s[i].lower() == "e": tokens.append("try-exponent")
            elif s[i].lower() in "abcdfghijklmnopqrstuvwxyz": tokens.append("letter")
            elif s[i] in "0123456789": 
                if (not tokens) or tokens[-1] != "digit": tokens.append("digit")

        if "letter" in tokens: return False
        if "signal" in tokens:
            ind_signals = [i for i in range(len(tokens)) if tokens[i] == "signal"]
            for i in ind_signals[::-1]:
                if i < len(tokens)-3 and tokens[i:i+4] == ["signal", "digit", "dot", "digit"]:
                    tokens[i:i+4] = ["decimal"]
                elif i < len(tokens)-2 and (tokens[i:i+3] == ["signal", "digit", "dot"] or tokens[i:i+3] == ["signal", "dot", "digit"]):
                    tokens[i:i+3] = ["decimal"]
                elif i < len(tokens)-1 and tokens[i:i+2] == ["signal", "digit"]:
                    tokens[i:i+2] = ["integer"]
        if "digit" in tokens:
            ind_digits = [i for i in range(len(tokens)) if tokens[i] == "digit"]
            for i in ind_digits:
                if i < len(tokens)-2 and tokens[i:i+3] == ["digit", "dot", "digit"]:
                    tokens[i:i+3] = ["decimal"]
                elif i < len(tokens)-1 and tokens[i:i+2] == ["digit", "dot"]:
                    tokens[i:i+2] = ["decimal"]
                elif i > 0 and tokens[i-1:i+1] == ["dot", "digit"]:
                    tokens[i-1:i+1] = ["decimal"]

        tokens = [t if t != "digit" else "integer" for t in tokens]

        if tokens[0] == "try-exponent" or tokens[-1] == "try-exponent": return False
        else:
            ind_exponent = [i for i in range(len(tokens)) if tokens[i] == "try-exponent"]
            for i in ind_exponent[::-1]:
                if tokens[i-1:i+2] == ["integer", "try-exponent", "integer"] or tokens[i-1:i+2] == ["decimal", "try-exponent", "integer"]:
                    tokens[i-1:i+2] = ["exponent"]

        if len(tokens) == 1 and tokens[0] in ["integer", "decimal", "exponent"]:
            return True
        return False