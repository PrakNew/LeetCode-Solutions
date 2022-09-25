class Solution:
    def floodFill(self, image, sr, sc, newColor):
        
        if image == [] or image[sr][sc]==newColor:
            return image
        
        m, n = len(image), len(image[0])
        
        q = [(sr, sc)]
        oldColor = image[sr][sc]
        
        while q:
            (x, y) = q.pop()
            image[x][y] = newColor
            
            for i, j in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
                if 0<=i<m and 0<=j<n and image[i][j]==oldColor:
                    q.append((i, j))
        
        return image