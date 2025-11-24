class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        freq = {}
        low = 0
        res = 0
        n = len(fruits)

        for high in range(n):
            freq[fruits[high]] = freq.get(fruits[high], 0) + 1
            while len(freq) > 2:
                freq[fruits[low]]-= 1
                if freq[fruits[low]]== 0:
                    del freq[fruits[low]]
                low +=1
            
            res = max(res,high - low + 1)
        return res