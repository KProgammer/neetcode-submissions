import copy 
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # here are my thoughts

        # brute force is to start with the first element and test all possible combinations and then repeate with the first element.

        # how it will work is that the cur_element inserts itself into the list and then before that looks at combining itself with the previous combinations and adds those cominations to the list. 
        
        # # initialize result list with an empty subset
        # res = [[]]

        # # initialize two pointers
        # # first is points to the current element in the input list and the second 
        # # points to the current element in the result list
        # res_i = 0

        # for num in nums:
        #     # Using the result pointer, insert combinations of previous elements and 
        #     # the new current element into the list up to the old end of the result 
        #     # list.
        #     res_len = len(res)
        #     for subind in range(0,res_len):
        #         # print("DEBUG:subset =",subset)
        #         # print("DEBUG:num =",num)
        #         subcopy = copy.deepcopy(res[subind])
        #         subcopy.append(num)
        #         res.append(subcopy)
        #         # print("DEBUG:res =",res)

        # return res

# What would happen if it wasn't in order
# [3, -1, 5]
# [[],[3]]
# [[],[3],[-1],[3,-1],[5],[3,5],[-1,5],[3,-1,5]]

        #solution
        res = []
        subset = []
        
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return

            # deicsion to include nums[i]
            subset.append(nums[i])

            dfs(i+1)

            # decision NOT to inlcude nums[i]
            subset.pop()
            dfs(i+1)

        dfs(0)
        return res