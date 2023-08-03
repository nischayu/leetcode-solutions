class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        result = ""
        for s in strs:
            result += str(len(s)) + "#" + s
        return result
        
    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """

        #General Case
        result = []
        ptr = 0
        curr_length = ""
        while(s):
            if(s[ptr] == "#"):
                decoded = s[ptr+1 : ptr + int(curr_length) + 1]
                result.append(decoded)
                s = s[ptr+int(curr_length) + 1:]
                ptr = 0

                curr_length = ""

            else:
                curr_length += s[ptr]
                ptr += 1

        #Base Case
        if(len(result) == 0):
            return [""]
        return result

        #The time complexity of this solution is O(n)
        #The space complexity of this solution is O(n)