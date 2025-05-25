class Solution(object):
    # TOPICS: STRING
    # Python <list>.index() built-in method does this exact job. It is necessary to wrap the method in a try-except clause because it throws an exception 
    # if the needle is not found.
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        try:
            return haystack.index(needle)
        except: 
            return -1