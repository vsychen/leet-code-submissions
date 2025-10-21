class Solution(object):
    # TOPICS: MATH
    # Generate a list of numbers from 1 to n and a dictionary to save the values already discovered. If an entry, with n as key, exists in the dictionary, return the value associated to n.
    # If not, walk the list getting the number of elements appearing before the current index (they are the nodes to the left) and recursively find the number of trees from that side. Do the
    # same for the number of elements appearing after the current index (they are the nodes to the right). Multiply the two values to get the number of possible combinations. When n is odd,
    # there's a need to add a last case, where both sides have the same length. In this case, get the value of one of the sides and then power it to the 2 (or multiply the value by itself).
    # The answer to numTrees(n) will be the sum of all combinations gotten from each position.
    # Note: remember to not multiply by 0 when the index is 0 or len(lst)-1. In these cases, change the value from zero to one, not impacting the multiplication.
    def numTrees(self, n):
        """
        :type n: int
        :rtype: List[Optional[TreeNode]]
        """
        ans = {0: 1, 1: 1, 2: 2}
        lst = [n for n in range(1, n+1)]

        if n in ans: return ans[n]
        else:
            r = 0
            for i in range(len(lst)>>1):
                left = len(lst[:i])
                right = len(lst[i+1:])
                r+=(self.numTrees(left)*self.numTrees(right))<<1
            
            if len(lst)%2 != 0:
                left = len(lst[:len(lst)>>1])
                aux = self.numTrees(left) 
                r += aux * aux

            ans[n] = r
            return ans[n]