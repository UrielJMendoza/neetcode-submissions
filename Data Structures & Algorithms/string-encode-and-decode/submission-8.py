class Solution:

    def encode(self, strs: List[str]) -> str:
        
        rev = []

        for word in strs:
            rev.append(str(len(word)) + "#" + word)

        return "".join(rev)
        

    def decode(self, s: str) -> List[str]:
        ##dec = ""

        strs = []
        i = 0

        while i < len(s):
            j = i

            # find the #
            while s[j] != "#":
                j += 1

            # get the length
            length = int(s[i:j])

            # get the word
            word = s[j + 1:j + 1 + length]
            strs.append(word)

            # move to next word
            i = j + 1 + length

        return strs