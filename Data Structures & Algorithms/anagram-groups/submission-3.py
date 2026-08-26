import string
import copy
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # so the idea behind this to create groups using a dictonary. The key of each group is the number of characters in each

        # This line creates a default dictionary which automatically assigns default values when a key that doesn't exist is entered
        result = defaultdict(list)

        # go through each string
        for string in strs:
            # determine a list of which characters are in the word
            char_list = [0]*26
            for c in string:
                # use the ascii characters to access the correct index
                # the list is stores how much of each character there is 
                char_list[ord(c)-ord("a")] += 1

            # Add word to the dictionary. Use a tuple since in python lists
            # can't be a key
            result[tuple(char_list)].append(string)
        
        return list(result.values())
