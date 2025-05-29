class Solution(object):
    # TOPICS: MATH/RECURSION
    # Generate a list with all numbers from 1 to n. For each recursion, pass this list and the k-th permutation to be returned. For each recursion, calculate the value of (n-1)! where
    # n will be the length of the list. Calculate the quotient and rest of k/((n-1)!). The quotient will determine which digit to add to the permutation, while the rest will define the
    # following digits. Remove the digit that was added to the permutation from the list and continue the recursion with the list (minus the digit used) and the rest of the division
    # as parameters.
    qtt = [0,1]
    def getQttPermutations(self, n):
        try:
            return self.qtt[n]
        except:
            permutations = n*self.getQttPermutations(n-1)
            self.qtt.append(permutations)
            return permutations

    def getKPermutation(self, lst, k):
        if k == 0: return lst[::-1]
        elif k == 1: return lst
        fact_n_minus_one = self.getQttPermutations(len(lst)-1)
        q = k//fact_n_minus_one
        r = k%fact_n_minus_one
        if r == 0: q -= 1
        d = lst[q]
        return [d] + self.getKPermutation([x for x in lst if x != d], r)

    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        lst = [str(i) for i in range(1,n+1)]

        if k == 1: return "".join(lst)
        elif k == self.getQttPermutations(n): return "".join(lst[::-1])
        else: return "".join(self.getKPermutation(lst, k))