class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        #Base case
        if(len(strs) == 1):
            return [strs]

        #General Case
        groups = {}
        for word in strs:
            counts = self.letter_counts(word)
            if(counts in groups):
                groups[counts].append(word)
            else:
                groups[counts] = [word]
        
        return groups.values()


    def letter_counts(self,word):
        letter_counts = [0] * 26
        for char in word:
            letter_counts[ord(char) - ord('a')] = letter_counts[ord(char) - ord('a')] + 1
        return tuple(letter_counts)

#The time complexity of this solution is O(mn*26)
#The space complexity of this solution is O(n)

### Optimized by using defaultdict(list)--------------------------------
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        #Base case
        if(len(strs) == 1):
            return [strs]

        #General Case
        groups = collections.defaultdict(list)
        for word in strs:
            counts = self.letter_counts(word)
            groups[counts].append(word)
        
        return groups.values()


    def letter_counts(self,word):
        letter_counts = [0] * 26
        for char in word:
            letter_counts[ord(char) - ord('a')] += 1
        return tuple(letter_counts)