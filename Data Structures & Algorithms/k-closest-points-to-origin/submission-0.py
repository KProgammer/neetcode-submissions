import numpy as np
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        # what have is a bunch of points that are varying distance and what I think would be great is to create an ordered list and then return up to k values. 

        ord_lst = []
        dst_lst = []

        for pt in points:
            # get the distance
            dist = self.get_dist(pt)
            print("DEBUG: dist =",dist)

            
            index = 0
            while index < len(dst_lst) and dist > dst_lst[index]:
                index += 1

            ord_lst.insert(index,pt)
            dst_lst.insert(index,dist)

        return ord_lst[:k]


    # This gets the distance from the origin
    def get_dist(self,p):
        x1, y1, x2, y2 = 0, 0, p[0], p[1]
        return np.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    