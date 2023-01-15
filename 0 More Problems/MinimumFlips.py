def bitVector(A):
    bit = ""
    for i in range(len(A)):
        for j in range(len(A[0])):
            bit += str(A[i][j])
    return bit

def getFlip(x, y, A, m, n):
    newState = ""

    for pos in range(len(A)):
        if pos in (x*m+y, (x+1)*m+y, (x-1)*m+y, x*m+y+1, x*m+y-1):
            if A[pos]=="1":
                newState+="0"
            else:
                newState+="1"
        else:
            newState += A[pos]
  
    # print("Original = ", A)
    # print("New state=", newState)

    return newState

# def minimumFlips(grid):
#     m, n = len(grid), len(grid[0])
#     visited = set()
#     q = [grid]
#     visited.add(bitVector(grid))
#     dist = 0
#     print(q)
#     while q:
#         size = len(q)
#         # print(q)
#         for _ in range(size):
#             if not q: # queue gets empty, solution found
#                 return dist
#             state = q[0]
#             print("Curr = ", state)
#             for i in range(m):
#                 for j in range(n):
#                     print(i, j, state)
#                     newState, bitvec = getFlip(i, j, state)
#                     if bitvec not in visited:
#                         # print(newState)
#                         q.append(newState)
#                         visited.add(bitvec)
#                         if bitvec=="0000":
#                             return dist
#                     print("Queue = ", q)
#             q.pop(0)
#         dist += 1
    
#     return -1
    
    


if __name__ =='__main__':
    # grid = [[1,1,1],[1,0,1],[0,0,0]]
    grid = [[0, 0], [0, 1]]
    m, n = len(grid), len(grid[0])
    
    # dist = minimumFlips(grid)

    q = []
    visited = set()
    bitvec = bitVector(grid)
    if not bitvec:
        print("Ans : 0")
    
    q.append(bitvec)

    dist = 0
    found = False
    while q:
        print(q)
        size = len(q)
        for _ in range(size):
            curr = q[0]

            if not curr:
                print("Ans = ", dist)
                found = True
                break 
            
            for i in range(m):
                for j in range(n):
                    bitvec = getFlip(i, j, curr, m, n)
                    if bitvec not in visited:
                        if bitvec=="0000":
                            found = True
                            break
                        visited.add(bitvec)
                        q.append(bitvec)
            
            q.pop(0)

        if found:
            break
        
        dist += 1
        

    if dist == 0:
        print("\nNo solution!!\n")
    
    print("\nFlips : ", dist)
    print()
