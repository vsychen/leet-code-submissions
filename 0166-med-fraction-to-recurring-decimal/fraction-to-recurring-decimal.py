class Solution:
    # TOPICS: STRING/MATH
    # If numerator is 0, return "0". If numerator is divisible by denominator without remainder, return 
    # the quotient of the division. If the quotient is not integer, first check the signal of both 
    # numerator and denominator. If both are negative, it's necessary to change the signal of both to
    # positive. If one of them is negative, it's necessary to change to positive and also change the
    # signal of the answer to negative. As for the division, add the first division result to the answer
    # (it will be the value before the dot). Add the dot and multiply the rest by ten (this will be the
    # new numerator). Create two lists one for the numerator/remainder and one for the quotient. While
    # the numerator/remainder is not zero and is not in the numerator/remainder list, execute the step-by-
    # step of the division repeatedly, appending both the quotient and the remainder to its respective
    # lists. At the end, if the numerator is 0, the division does not have a repeating part, a simple 
    # concatenation between the answer and the list of quotients is enough. But if the numerator is not 0,
    # there's a repeating part. Find the index of the current numerator in the list of numerator/remainders.
    # Using this index as pivot, everything before it in the quotient list is not repeating, and can be
    # directly appended to the answer. Everything after the index, however, belongs to the repeating part.
    # Concatenate it and put them between parenthesis before appending to the answer.
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0: return "0"
        elif numerator%denominator == 0: return str(int(numerator/denominator))
        else:
            answer = ""

            if numerator < 0:
                answer = "-"
                numerator = 0-numerator
            if denominator < 0:
                answer = "" if answer == "-" else "-"
                denominator = 0-denominator

            answer += str(int(numerator/denominator)) + "."
            numerator = (numerator%denominator)*10
            n_lst = []
            q_lst = []

            while numerator != 0 and numerator not in n_lst:
                n_lst.append(numerator)
                if numerator > denominator: q_lst.append(str(int(numerator/denominator)))
                else: q_lst.append("0")
                numerator %= denominator
                if numerator != 0: numerator *= 10
            
            if numerator == 0: answer += "".join(q_lst)
            else:
                i = n_lst.index(numerator)
                answer += "".join(q_lst[:i]) + "(" + "".join(q_lst[i:]) + ")"
            return answer