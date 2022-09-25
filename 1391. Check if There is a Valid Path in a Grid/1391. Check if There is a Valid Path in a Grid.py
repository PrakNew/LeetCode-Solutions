def hasValidPath(self, grid: List[List[int]]) -> bool:
        
        directions = {1 : [1, 4], 2:[2, 3], 3:[1, 3], 4:[4, 3], 5:[2, 1], 6:[2, 4]}
        final_directions = { (3, 1): 2, (3, 3): 4, (4,3): 1, (4,4): 2, (5,2): 4, (5,1): 3, (6,2): 1, (6,4): 3}
        
        m, n = len(grid), len(grid[0])
        
        x, y = 0, 0
        
        dir1, dir2 = directions[grid[0][0]][0], directions[grid[0][0]][1]
        
        curr_dir = None
        
        if grid[0][0] in [1, 6]:
            curr_dir = 1
        elif grid[0][0] in [2, 3, 4]:
            curr_dir = 2
        else: # 5
            return False
            
        
        while 0<=x<m and 0<=y<n:
            
            if x==m-1 and y==n-1:
                return True
            
            if curr_dir==1:
                # print("Right cell")
                # print(curr_dir, x, y+1, grid[x][y+1])
                # check initial direction of the cell on right
                if 0<=x<m and 0<=y+1<n and curr_dir in directions[grid[x][y+1]]:
                    y+=1
                else:
                    return False
            
            elif curr_dir==2:
                # print("Below cell")
                # check initial direction of the below cell 
                if 0<=x+1<m and 0<=y<n and curr_dir in directions[grid[x+1][y]]:
                    x+=1
                else:
                    return False
            
            elif curr_dir==3:
                # print("Top cell")
                # check initial direction of the top cell 
                if 0<=x-1<m and 0<=y<n and curr_dir in directions[grid[x-1][y]]:
                    x-=1
                else:
                    return False
            
            else: # dir = 4
                # print("Left cell")
                # check initial direction of the cell on left
                if 0<=x<m and 0<=y-1<n and curr_dir in directions[grid[x][y-1]]:
                    y-=1 # move to the cell
                else:
                    return False
            
            # prev_dir = curr_dir
            # print(curr_dir)
            
            # for 1 and 2 direction remains same
            if grid[x][y] in [1, 2]:
                continue

            curr_dir = final_directions[(grid[x][y], curr_dir)]

        
        return False