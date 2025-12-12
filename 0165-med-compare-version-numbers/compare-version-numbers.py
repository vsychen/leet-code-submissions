class Solution(object):
    # TOPICS: STRING
    # Split the two strings version1 and version2 with the delimiter '.'. While both lists has elements, pop the first one of each list and compare them.
    # If the element from version1 is smaller, return -1. If it's bigger, return 1. After the iterations, if there's still elements in any of the lists,
    # check if they are zeros. If there are something other than zeros in version1, return 1. If there are something other than zeros in version2, return -1.
    # Otherwise, return 0.
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        lst1 = version1.split(".")
        lst2 = version2.split(".")

        while lst1 and lst2:
            l1 = int(lst1.pop(0))
            l2 = int(lst2.pop(0))
            if l1 < l2: return -1
            elif l1 > l2: return 1

        if lst1 and any([True for l in lst1 if int(l) != 0]): return 1
        elif lst2 and any([True for l in lst2 if int(l) != 0]): return -1

        return 0