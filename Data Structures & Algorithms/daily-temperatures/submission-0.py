class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        max_id = 0
        l = temperatures
        i = 0
        result = []
        while i < len(l) - 1:
            max_id = 0
            m = 0
            j = i + 1
            while j < len(l):
                if l[i] < l[j]:
                    last_one = m
                    m = max(m,l[j])
                    if m != last_one:
                        max_id = j - i
                    break
                j += 1
            result.append(max_id)
            i += 1
        result.append(0)
        return result
                