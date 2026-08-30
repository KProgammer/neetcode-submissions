# include <iostream>
# include <queue>

class Solution {
public:
    // recursion function
    void bfs(int r, int c, vector<vector<char>>& grid){
        // if it is not a valid point or water
            // return 
        // std::cout << "DEBUG: r,c" << r << " " << c << std::endl; 
        if ((r < 0) || (c < 0) || (r >= grid.size()) || (c >= grid[r].size()) 
            || (grid[r][c] == '0')) {
                return;
            }
        // mark as water
        grid[r][c] = '0';

        // go up,down,left,right
        bfs(r-1,c, grid);
        bfs(r+1,c, grid);
        bfs(r,c-1, grid);
        bfs(r,c+1, grid);
    }

    int numIslands(vector<vector<char>>& grid) {
        if (grid.empty()){
            return 0;
        }
         
        // integer to counter the number of islands
        int num_islands{};

        
        // for each element
            // if it is a 1
                // recursively check for the island and mark as found
                // increase the number of islands counter
            // if it is not a 1
                // skip it
        for (int row = 0; row < grid.size(); row++) {
            for (int col = 0; col < grid[row].size(); col++){
                if (grid[row][col] == '1'){
                    bfs(row,col,grid);
                    num_islands++;
                }
            }
        }

        return num_islands;

        
    }
};
