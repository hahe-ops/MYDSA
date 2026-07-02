"""Given a matrix mat[][], the task is to find the sum of all the elements of the matrix.
Examples:
Input: mat[][] = {{1, 2, 3}, {4, 5, 6}}
Output: 21
Explanation: Here sum of all element = 1 + 2 + 3 + 4 + 5 + 6 = 21"""

m=[[1,2,3],[4,5,6],[7,8,9]]
s=0
for i in m:
    for j in i:
        s=s+j

print("sum: ", s)
