class Solution(object):
    # TOPICS: MATH
    # Get all powers of 5 less than n. Initialize a counter equal to 0. For each value in the powers' list, divide n by the power and add the integer quotient to 
    # the counter.
    # Explanation: a number will have a trailing zero if and only if it's divisible by 10. Or divisible by 2 and 5. The factorial works in a way that each two 
    # numbers it will add one '2' to the prime factorization of the number. Meaning it depends on the '5's to determine how many '10's the number can be divided 
    # without leaving remainder. But there are times a number earns more than 1 '5' to its prime factorization (when it's multiplied by 5^n, like 25, 125, etc.). 
    # When dividing n by each element in the powers' list, it will account for this offset. For example, if n is 30 (30*29*28*...*3*2*1), 30//5 = 6, 30//25 = 1.
    # 6+1 = 7, there will be 7 trailing zeroes. It would be 6 zeroes if not for the 25 appearing somewhere in the factorial. One '5' is already accounted for,
    # so only one '5' is needed to be added to the counter.
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        powers = [1, 5]
        while powers[-2]*5 < n:
            powers.append(powers[-1]*5)
        powers.pop(0)

        count = 0
        for p in powers:
            count += n//p
        return count