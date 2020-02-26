class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        length = len(trips)
        if(length == 0):
            return True
        new_trips = sorted(trips, key = lambda x:x[1])
        # print(new_trips)
        load_num = [0 for i in range(1001)]
        for i in range(length):
            num_people = new_trips[i][0]
            start = new_trips[i][1]
            end = new_trips[i][2]
            # print(start, end)
            if(load_num[start] + num_people > capacity):
                return False
            # load_num[start:end-start] += [num_people for j in range(end-start)]
            for j in range(start, end):
                load_num[j] += num_people
            # print(load_num)
        return True