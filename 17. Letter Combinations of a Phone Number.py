class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if(len(digits) == 0):
            return ""
        alphabet = [[''],[''],['a','b','c'],['d','e','f'],['g','h','i'],['j','k','l'],['m','n','o'],['p','q','r','s'],['t','u','v'],['w','x','y','z']]

        answer = []
        length = len(digits)
        count = 0
        temp = int(digits[0])
        print(temp)
        for element in alphabet[temp]:
            answer.append(element)
        print(answer)
        for i in range(1, length):
            temp = int(digits[i])
            temp_length = len(alphabet[temp])
            ori_length = len(answer)
            answer = answer * temp_length
            count = 0
            count1 = 0
            for j in range(len(answer)):
                # print(element)
                answer[j] += alphabet[temp][count]
                count1 += 1
                if(count1 == ori_length):
                    count1 = 0
                    count += 1
        return answer
                