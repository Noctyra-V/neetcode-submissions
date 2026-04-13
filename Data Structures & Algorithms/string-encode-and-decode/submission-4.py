
class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += ''.join(f'{ord(c):02x}' for c in s)
            res += "-"
        return res

        return res
    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        s = s[:-1]
        res = s.split("-")
        result = []
        for a in res:
            string = ''.join(chr(int(a[i:i+2], 16)) for i in range(0, len(a), 2))
            result.append(string)
        return result