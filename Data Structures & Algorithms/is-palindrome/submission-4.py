import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # smims (quick example)
        
        # Create translation table
        translator = str.maketrans('', '', string.punctuation)

        # Remove punctuation
        s = s.translate(translator)

        # make s lowercase
        s = [a.lower() for a in s]
        s = ''.join(s)
        print("DEBUG: s =",s)

        # initialize variables to serve as indices.
        # They will be initialized as the beginning and end of the string
        a = 0
        b = len(s)-1

        print("DEBUG: a =",a)
        print("DEBUG: b =",b)

        # while they don't equal each other or a != b
        while (a < b):
            # make sure a and b are alphanumeric before comparing
            while(not s[a].isalnum()):
                a += 1
            while(not s[b].isalnum()):
                b -= 1

            # compare characters at indices a and b
            # if true, increment a and decrement b
            print("DEBUG: a =",a)
            print("DEBUG: b =",b)
            print("DEBUG: s[a] =",s[a])
            print("DEBUG: s[b] =",s[b])
            if ((s[a] == s[b]) and (a < b)):
                a += 1
                b -= 1
                   
            elif(s[a] == s[b]):
                return True
            
            # else: return false
            else:
                return False

        return True

        