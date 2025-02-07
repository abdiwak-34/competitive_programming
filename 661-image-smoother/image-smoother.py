class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        n, m = len(img), len(img[0])
        n_img = [[0]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                sumof = img[i][j]
                count = 1
                if i-1 >= 0 and j-1>=0:
                    sumof +=img[i-1][j-1]
                    count +=1
                if j-1 >= 0:
                    sumof +=img[i][j-1]
                    count +=1
                if i+1 < n and j-1>=0:
                    sumof +=img[i+1][j-1]
                    count +=1
                if i-1 >= 0:
                    sumof +=img[i-1][j]
                    count +=1
                if i+1 < n:
                    sumof +=img[i+1][j]
                    count +=1
                if i-1 >= 0 and j+1 <m:
                    sumof +=img[i-1][j+1]
                    count +=1
                if j+1 < m:
                    sumof +=img[i][j+1]
                    count +=1
                if i+1 < n and j+1 < m:
                    sumof +=img[i+1][j+1]
                    count +=1
                n_img[i][j] = sumof//count

        return n_img
                