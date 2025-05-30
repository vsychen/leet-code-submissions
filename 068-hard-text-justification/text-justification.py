class Solution(object):
    # TOPICS: STRING
    # Add the maximum quantity of words possible to a row without crossing the maxWidth limit (adding one space after each word) and remember to clear the last space added 
    # (there won't be words after the last space, need to remove it). For each row, calculate the length of the current string and the quantity of spaces. Get the difference
    # between the maxWidth and the current row, this difference will be added as extra spaces. To calculate the number of space characters each space should have, divide
    # the remaining characters by the quantity of spaces the row will have and distribute accordingly (if the division is not exact, the last spaces will have 1 space
    # character less). The first special case is when the row has only one word (there's no space characters in the row). In this case, add space characters at the end of 
    # the row until it reaches the maxWidth length. The second special case is the last row, the extra spaces will be added at the end of the row even if there's spaces in
    # between its words.
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        aux = []
        aux_aux = ""
        for w in words:
            if len(aux_aux) + len(w) <= maxWidth:
                aux_aux += (w + " ")
            else:
                aux.append(aux_aux[:-1])
                aux_aux = w + " "
        aux.append(aux_aux[:-1])

        r = []
        
        for i in range(len(aux)):
            row_length = len(aux[i])
            row_spaces = sum([1 for c in aux[i] if c == " "])
            remaining = maxWidth - row_length
            if i < len(aux)-1 and row_spaces != 0:
                quotient = remaining//row_spaces
                rest = remaining%row_spaces
                spaces = ["".join(" " for _ in range(quotient+2)) for _ in range(rest)]
                spaces.extend(["".join(" " for _ in range(quotient+1)) for _ in range(row_spaces-rest)])
                words = aux[i].split(" ")
                new_substring = ""
                while words:
                    new_substring += words.pop(0)
                    if spaces: new_substring += spaces.pop(0)
                r.append(new_substring)
            else:
                row_spaces = "".join(" " for _ in range(maxWidth-row_length))
                r.append(aux[i]+row_spaces)
        return r