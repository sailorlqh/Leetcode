from collections import Counter
class Solution(object):
    def minDominoRotations(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        dict_a = Counter(A)
        dict_b = Counter(B)
        dict_c = dict_a + dict_b
        new_dict = sorted(dict_c.items(), key = lambda item:item[1])
        key = new_dict[-1][0]
        count = new_dict[-1][1]
        if(count < len(A)):
            return -1
        flip_a = 0
        flip_b = 0
        for i in range(len(A)):
            if(A[i] == key and B[i] == key):
                continue
            elif(A[i] == key):
                flip_a += 1
            elif(B[i] == key):
                flip_b += 1
            else:
                return -1
        return min(flip_a, flip_b)
                        
        # return min_count if  min_count != None else -1
        