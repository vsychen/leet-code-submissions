class Solution(object):
    # TOPICS: ARRAY/GREEDY
    # If there's only one gas station, check if gas[0] is greater than cost[0], to be able to go back to that station. Make a new list where each element
    # lst[x] is gas[x]-cost[x]. If the total sum of the new list is less than 0, there's not enough gas to complete the circuit. Group together consecutive
    # positive/negative values in the new list and save the index each time a new positive value group appear, or -1 each time a new negative value group
    # appear, just to keep the index list consistent with the values list. Then, for each of the positive starting points, simulate the trip around the
    # circuit. If the value drops below zero, that starting point fails, try the next one. If all positive starting points fail, there's not a successful
    # path to take, return -1. If a positive starting point works, return it as the answer.
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if len(gas) == 1: return 0 if gas[0] >= cost[0] else -1
        aux = [gas[i]-cost[i] for i in range(len(gas))]
        if sum(aux) < 0: return -1
        index = []
        queue = []

        for i in range(len(aux)):
            if not queue:
                queue.append(aux[i])
                if aux[i] >= 0: index.append(i)
                else: index.append(-1)
            else:
                if (queue[-1] < 0 and aux[i] < 0) or (queue[-1] >= 0 and aux[i] >= 0):
                    queue[-1] += aux[i]
                else:
                    queue.append(aux[i])
                    if aux[i] >= 0: index.append(i)
                    else: index.append(-1)

        answer = -1

        for i in range(len(queue)):
            if queue[i] > 0:
                queue2 = queue[i:]+queue[:i]

                local_sum = 0
                for n in queue2:
                    local_sum += n
                    if local_sum < 0: break
                
                if local_sum >= 0: answer = index[i]
            
            if answer != -1: break

        return answer