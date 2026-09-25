class Solution:

    def encode(self, strs: List[str]) -> str:

        s = ""
        for word in strs:
            s += str(len(word)) + "#" + word
        
        return s

    def decode(self, s: str) -> List[str]:

        result = []
        i = 0
        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1
            
            length = int(s[i:j])
            wordStart = j + 1
            wordEnd = wordStart + length

            result.append(s[wordStart:wordEnd])

            i = wordEnd
        return result

