class Solution(object):
    # TOPICS: ARRAY/COUNTING
    # Use Boyer-Moore Majority Voting Algorithm. Get a variable to count the "votes" as well as one variable to keep track of the "candidate". Every time the number
    # of votes is 0, update the candidate as well as add one count of vote (current vote). If the vote is the same as the current candidate, add one to the counter.
    # If the vote is different than the current candidate, decrease the count. At the end of the run, in the worst case there will be n+1 votes for the majority while
    # n votes for the rest of the elements (doesn't matter if the rest of the elements are different or the same element).
    # Example: [1,1,5,1,5,1,5,5,x]. In this example, 1 will be the candidate for the most part of the list, while votes will wave between 1 and 2. The moment votes go 0
    # (index = 7) means count(1) = count(5). The value of x then decides the majority (if x = 1, the majority will be 1. if x = 5, majority will be 5. can't be any
    # other number because of question constraints; there must be a value/candidate that is majority in the group)
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        votes = 0
        candidate = None
        for i in range(len(nums)):
            if votes == 0:
                candidate = nums[i]
                votes += 1
            elif nums[i] == candidate:
                votes += 1
            elif nums[i] != candidate:
                votes -= 1
        
        return candidate