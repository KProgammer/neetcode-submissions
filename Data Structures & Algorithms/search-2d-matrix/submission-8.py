import numpy as np
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # I need to create program that solves in log(m*n) time. This, I believe, requires that I use a binary search. 

        # I will use two pointers (a,b) and (c,d) starting at the corners (0,0) and  (m,n). These will iterate by halving the available rows and columns based on whether the values are greater or less than the target

        # initialize pointers
        a, b, c, d = 0, 0, len(matrix)-1, len(matrix[0])-1
        
        # initialize dist between points
        dist_btw_points = 1

        while (dist_btw_points):
            print("DEBUG: started loop")
            
            # get the half way point
            # print("DEBUG: len(matrix[0]) =",len(matrix[0]))
            # print("DEBUG: len(matrix) =",len(matrix))
            # print("DEBUG: c*len(matrix[0])+d=",c*len(matrix[0])+d)
            # print("DEBUG: (a*len(matrix[0])+b)=",(a*len(matrix[0])+b))

            dist_to_p1 = (a*len(matrix[0])+b)
            dist_to_p2 = (c*len(matrix[0])+d)

            dist_btw_points = round((dist_to_p2 - dist_to_p1)//2)
            mid_length = dist_to_p1 + dist_btw_points
            midrow = (mid_length // len(matrix[0]))
            midcol = (mid_length % len(matrix[0]))
            print("DEBUG: mid_length =",mid_length)
            print("DEBUG: midrow =",midrow)
            print("DEBUG: midcol =",midcol)

            print("DEBUG: matrix[midrow][midcol] =",matrix[midrow][midcol])
            # if (a,b) or (a,c) are at the target
            if (matrix[a][b] == target) or (matrix[c][d] == target) or (matrix[midrow][midcol] == target) :
                return True

            # matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10
            # (0,0) (2,3)
            # length = ((8+3)-(0+0))/2 = 5
            # midrow = (5//4) = 1
            # midcol = (5%4) = 1
            # matrix[1][1]=11 and c = 1, d = 1
            # length = ((4+1)-(0+0))/2 = 2
            # midrow = (2//4) = 0
            # midcol = (2%4) = 2
            # matrix[0][2] = 4 a = 0 b = 2
            # length = ((4+1)-(0+2))/2 = 1
            # midrow = (1//4) = 0
            # midcol = (1%4) = 1
            # matrix[0][1] = 10 a = 1 b = 2
            # 3*4 = 12 12/2 = 6 6//4 = 1 6%4 = 2

            # lenght of 12
            # a = 0 b = 11
            # half way is 5 str[5] = 6 which is less than 10
            # a = 6 b = 11
            # halfway is ((6-11)/2) + 6 = 8  

            
            # if it is less than the target, look in the upper half
            if matrix[midrow][midcol] < target :
                a = midrow #int(np.ceil((a)+((c-a)/2)))
                b = midcol
                print("DEBUG: a =",a)
                print("DEBUG: b =",b)
            # otherwise look in the lower half
            else:
                c = midrow
                d = midcol 
                print("DEBUG: c =",c)
                print("DEBUG: d =",d)

        return False

        # # solution
        # ROWS, COLS = len(matrix), len(matrix[0])
        # top, bot = 0, ROWS-1
        # while top <= bot:
        #   row = (top+bot)//2
        #   if target > matrix[row][-1]:
        #       top = row + 1  
        #   elif target < matrix[row][0]:
        #       bot = row - 1
        #   else: 
        #        break

        # if not (top <= bot):
        #   return False
        
        # row = (top+bot)//2
        # l, r = 0, COLS-1
        # while l <= r:
        #   m = (l + r) // 2
        #   if target > matrix[row][m]:
        #       l = m+1
        #   elif target < matrix[row][m]:
        #       r = m-1
        #   else:
        #       return True
        # return False
