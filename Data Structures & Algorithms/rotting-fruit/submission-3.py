class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        m,n=len(grid), len(grid[0])
        q=deque()
        fresh=0
        t=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    fresh+=1
                elif grid[i][j]==2:
                    q.append((i,j))
        
        dirs = [(1,0),(0,1),(-1,0),(0,-1)]
        while q and fresh>0:
            for i in range(len(q)):
                i,j = q.popleft()
                
                for dx,dy in dirs:
                    x,y = i+dx,j+dy
                    if 0<=x<m and 0<=y<n and grid[x][y]==1:
                        fresh-=1
                        grid[x][y]=2
                        q.append((x,y))
                
            t+=1
        return t if fresh==0 else -1

