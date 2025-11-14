class UnionFind(object):
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [0]*size
        self.size = [1]*size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return
        
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        self.size[root_x] = self.size[root_y] = self.size[root_x]+self.size[root_y]
    
    def getLargestSize(self):
        return max(self.size)

class Solution(object):
    # TOPICS: ARRAY/HASH TABLE/UNION FIND
    # Use Union-Find data structure to create disjoint sets. Add a size list in addition to parent and rank lists.
    # If nums is empty, return 0. Turn nums into a set with values as keys and an index as value. Use this set to create the Union-Find.
    # For each value in the set, see if value-1 and value+1 are also in the set. If yes, unite these in the Union-Find data structure. If they
    # are not, skip. At the end, the sets will be grouped by the consecutive values. Get the size of the largest set and return as the answer.
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        value_to_index = {val:i for i,val in enumerate(set(nums))}
        aux = UnionFind(len(value_to_index))

        for n in value_to_index:
            if n-1 in value_to_index:
                aux.union(value_to_index[n-1], value_to_index[n])
            
            if n+1 in value_to_index:
                aux.union(value_to_index[n], value_to_index[n+1])
        
        return aux.getLargestSize()