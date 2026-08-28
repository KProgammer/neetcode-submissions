class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # make the grid a class object
        self.grid = grid

        # mark water and land variables
        self.WATER = "0"
        self.LAND = "1"
        
        # index to store num of islands
        num_islands = 0

        # dictionary to store the island locations and what numbered island they are 
        # a part of
        self.land_dict = {}

        height = len(grid)
        width = len(grid[0])

        # def get_island(row, col, width, height):
            # # print("DEBUG: (row, col) =",(row,col))
            # # print("DEBUG: grid[row][col] =",self.grid[row][col])
            # # print("DEBUG: self.grid", self.grid)
            # # check if it's a valid point or water
            # if row < 0 or col < 0 or row >= height or col >= width \
            # or self.grid[row][col] == self.WATER or\
            # self.grid[row][col] == "x":
            #     return 
            
            # # if it's land mark it as discovered
            # # elif self.grid[row][col] == self.LAND:
            # self.grid[row][col] = "x"
            
            # # search up, down, left, and right
            # # if self.valid_pt(row+1,col):
            # #     return self.get_island(row+1,col)  # down
            # # if self.valid_pt(row-1,col):
            # #     return self.get_island(row-1,col) # up
            # # if self.valid_pt(row,col+1):
            # #     return self.get_island(row,col+1)  # right
            # # if self.valid_pt(row,col-1): 
            # #     return self.get_island(row,col-1)  # left
            
            # get_island(row+1,col, width, height) # down
            # get_island(row-1,col, width, height) # up
            # get_island(row,col+1, width, height) # right
            # get_island(row,col-1, width, height) # left

        # for each coordinate
        for row in range(0,len(grid)):
            for col in range(0,len(grid[row])):
                
                # print("DEBUG: not (row,col) in self.land_dict =",not (row,col) in self.land_dict)
                # print("DEBUG: grid[row][col] == self.LAND =",grid[row][col] == self.LAND)
                # if it's a piece of unclaimed land
                # print("DEBUG: self.grid before",self.grid)
                if grid[row][col] == self.LAND:
                    num_islands += 1
                    self.get_island(row,col)
                    # self.get_island(row,col,width,height)
                    # get_island(row,col,width, height)
        # return the number of islands
        return num_islands
        

                
    
    def valid_pt(self,row,col):
        # row and col must be greater then zero
        # row must be < len(grid) and col must be < len(grid[0])
        return row >= 0 and col >= 0 \
        and row < len(self.grid) and col < len(self.grid[0])

    # def get_island(self, row, col, width, height):
    def get_island(self, row, col):
        # print("DEBUG: (row, col) =",(row,col))
        # print("DEBUG: height =",height)
        # print("DEBUG: grid[row][col] =",self.grid[row][col])
        # print("DEBUG: self.grid", self.grid)

        # check if it's a valid point or water
        # if row < 0 or col < 0 or row >= height or col >= width \
        if not self.valid_pt(row,col) \
        or self.grid[row][col] == self.WATER or\
        self.grid[row][col] == "x":
            return 
        
        # if it's land mark it as discovered
        # elif self.grid[row][col] == self.LAND:
            # self.grid[row][col] = "x"
        self.grid[row][col] = "x"
        
        # self.get_island(row+1,col, width, height) # down
        # self.get_island(row-1,col, width, height) # up
        # self.get_island(row,col+1, width, height) # right
        # self.get_island(row,col-1, width, height) # left

        self.get_island(row+1,col) # down
        self.get_island(row-1,col) # up
        self.get_island(row,col+1) # right
        self.get_island(row,col-1) # left


    
    def get_land_num(self,row,col):
        # look at neighbors and see if  on the edge of the see or traveled region
        
        # look up and down
        for i in range(-1,2,2):
            print("(row+i,col)",(row+i,col))
            print("self.valid_pt(row+i,col)",self.valid_pt(row+i,col))
            if self.valid_pt(row+i,col) and (row+i,col) in self.land_dict:
                return self.land_dict[(row+i,col)]
        # look left and right
        for j in range(-1,2,2):
            print("(row,col+j)",(row,col+j))
            print("self.valid_pt(row,col+j)",self.valid_pt(row,col+j))
            if self.valid_pt(row,col+j) and (row,col+j) in self.land_dict:
                return self.land_dict[(row,col+j)]
        
        return 0



    # here's my over all idea: go to a point, follow the island around until you have found all the edges, mark those areas as travled, and then return to the closes point. 

    # if it's land, look up, down, left, and right 
        