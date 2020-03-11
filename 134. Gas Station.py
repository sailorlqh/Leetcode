class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start_station = 0
        total_tank = 0
        tank = 0
        for i in range(0, len(gas)):
            total_tank += gas[i] - cost[i]
            tank += gas[i] - cost[i]
            if(tank < 0):
                start_station = i + 1
                tank = 0
        return start_station if total_tank >= 0 else -1