class Solution(object):
    # TOPICS: STRING
    # The codes are numbers from 1 to 26 and, as such, the valid combinations should have (i) any number from 1 to 9, (ii) a '1' followed by any number from 1 to 9, 
    # (iii) a '2' followed by any number from 1 to 6, and (iv) '10' and '20'. For this question, the number of combinations of consecutive 'can be combined' characters 
    # follow a fibonacci distribution, i.e., '12121' can have fib(5) possible results.
    # In the case of partially combination, the character should be included in the fibonacci calculation, but reset afterwards, i.e., '12191' will result in fib(4)*fib(1).
    # If the character cannot be combined, exclude it from the fibonacci calculation, and reset the counter afterwards, i.e., '12911' will result in fib(2)*fib(2).
    # If there's a zero lost in the codes, check if it's accompanied by a '1' or '2'. if it is, it cannot leave the '1' or '2' side, i.e., '12012' should be treated as 
    # '1' + '20' + '12' and result in fib(1)*fib(2).
    # The 'cannot be combined' characters such as '10', '20', '9', etc. should not reset the calculation (the multiplication counter should not multiply by 0)
    # With these premises, if the string starts with a zero, or if there are multiple consecutive zeroes, it's a dud; return 0. separate the string in tokens (to consider 
    # each character separately, with the exception of '0', as they cannot be alone. if they are alone, it's a dud, return 0). Then, walk the list of tokens checking the 
    # characters. If it's '1' or '2', increment the add_counter. If it's '3' to '6', increment the add_counter, get fib(add_counter). If the character is '7' to '9', 
    # same behavior as '3' to '6' if its following a '1', otherwise, just get fib(add_counter) without incrementing first. for any other situation, get fib(add_counter) 
    # without incrementing first. Every time the res_counter multiply by fib(add_counter), reset the add_counter. The multiplication should not occur if add_counter is 0.
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s[0] == '0' or '00' in s: return 0

        # Initializing fibonacci sequence and method
        fib = {1:1, 2:2, 3:3, 4:5, 5:8, 6:13}

        def fibonacci(n):
            if n in fib: return fib[n]
            else:
                fib[n] = fibonacci(n-1) + fibonacci(n-2)
                return fib[n]

        # Divide the string in tokens (the 0 should be paired with another digit, and it will always be '1' or '2')
        i = len(s)-1
        ps = []
        while i >= 0:
            if s[i] == '0':
                i -= 1
                if s[i] not in ['1','2']:
                    return 0
                else:
                    ps.append(s[i]+'0')
            else:
                ps.append(s[i])
            i -= 1
        
        add_counter = 0
        res_counter = 1
        for i in range(len(ps)-1, -1, -1):
            digit = ps[i]

            if digit in ['1','2']:
                add_counter += 1
            else:
                if digit in ['3','4','5','6'] or (digit in ['7','8','9'] and i+1 < len(ps) and ps[i+1] == '1'):
                    add_counter += 1
                if add_counter != 0: res_counter *= fibonacci(add_counter)
                add_counter = 0
        if add_counter != 0: res_counter *= fibonacci(add_counter)
        return res_counter