class Solution(object):
    # TOPICS: MATH
    # To reduce the calculations in this question, use a dictionary with a pair (m,n) as the key and the number of combinations as the value. To reduce the quantity of storage needed for
    # the question, order the m and n values. If m == 1, there's only one path from START to END (a straight line). If m == 2, there's n paths from START to END. For m >= 3, calculate
    # the quantity of paths for (m-1, n) and (m, n-1) and add them. Special case, m == n, the result will be two times the quantity of paths for (m-1, n).
    paths = {}
    def doTheTrick(self, m, n):
        m,n = min(m,n), max(m,n)
        r = -1
        try:
            r = self.paths[(m, n)]
        except:
            if m == 1: r = 1
            elif m == 2: r = n
            else:
                if m == n: r = (self.doTheTrick(m-1, n)<<1)
                else: r = self.doTheTrick(m-1,n)+self.doTheTrick(m,n-1)
            self.paths[(m,n)] = r
        finally:
            return r

    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        return self.doTheTrick(m,n)