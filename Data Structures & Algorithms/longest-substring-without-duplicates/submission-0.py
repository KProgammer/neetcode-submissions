class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # thought 1, use a dictionary to store the characters inside a dictionary so you can tell which characters are in the substring. 

        # I have thought of using a moving window to find the longest substring

        # Example would be "zxyzxyz"
        #                     | |
        # dict{z:3,,y:2}
        # sub_len = 3, l = 1, r=4

        # initialize pointer indices
        l = 0
        r = 0

        # dictionary to store the substring
        sub = {}

        # store longest substring length
        sub_len = 0

        # while right hasn't reached the end
        while (r < len(s)):
            
            # if character on the right isn't in the substring add it
            if(not s[r] in sub):
                # record it's index
                sub[s[r]] = r
                
            
            # else if it is in the substring
            elif(s[r] in sub):
                
                # since we still need to use the current position of l, I 
                # will use this variable to hold the new index of l temporarily
                temp_l = sub[s[r]]+1

                # move left pointer to right of the first appearance of the
                # repeated character
                for ind in range(l,sub[s[r]]+1):
                    del(sub[s[ind]])
                # update the l index
                l = temp_l

                # update the new position of the repeated value
                sub[s[r]] = r

            # increase value of r
            r += 1
            
            # update longest length
            if((r-l) > sub_len):
                sub_len = (r-l)

        return sub_len


