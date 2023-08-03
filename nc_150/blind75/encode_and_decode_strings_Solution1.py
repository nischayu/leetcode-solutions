class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        result_str = ""

        for s in strs:
            result_str += str(len(s)) + "#" + s
        return result_str
        
        #The time complexity of this solution is O(n)
        #The space complexity of this solution is O(n) 
        
    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        result = []

        curr_length = ""
        print(s)
        ptr = 0
        while ptr < len(s):
            if s[ptr] != "#": #number encounted
                curr_length += s[ptr]
                ptr += 1
            else: # # encountered at pos i
                print("# found")
                word = s[ptr + 1: ptr + int(curr_length)  + 1]
                result.append(word)
                ptr = ptr + int(curr_length) + 1
                curr_length = ""
        return result


    #Lesson learned: when you have a for loop for i, cannot set i to something else
    #The time complexity of this solution is O(n)
    #The space complexity of this solution is O(n)