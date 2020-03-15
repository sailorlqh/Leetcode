class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        ans = {}
        for element in strings:
        	temp = ''
        	for i in range(1, len(element)):
        		a = ord(element[i]) - ord(element[i-1])
        		if(a < 0):
        			temp += str(a + 26)
        		else:
        			temp += str(a)
        	if(temp not in ans.keys()):
        		ans[temp] = [element]
        	else:
        		ans[temp].append(element)
        return ans.values()