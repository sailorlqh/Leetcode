class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp = {}
        ans = []

        length = len(strs)
        for i in range(length):
        	sortedStr = ''.join(sorted(strs[i]))
        	word_sum = sortedStr
        	if(word_sum not in temp.keys()):
        		temp[word_sum] = [strs[i]]
        	else:
        		temp[word_sum].append(strs[i])
       	# print(temp)
        # for key in temp.keys():
        	# ans.append(temp[key])
        return temp.values()