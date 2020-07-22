#!/usr/bin/env python3

'''
  If an element in MxN matrix is zero(0), replace whole row and column with zero(0)
'''

C = int(input("Columns:"))
R = int(input("Rows:"))

row,col = [],[]

M = [[int(input()) for x in range (C)]for y in range(R)]
N = M

print("Original matrix:")
for i in range(R):
  for j in range(C):
    print(M[i][j], end = " ")
    if M[i][j] == 0:
      row.append(i)
      col.append(j)
  print()
  

print("Resultant matrix:")
for i in range(R):
  for j in range(C):
    if i in row or j in col:
      M[i][j] = 0
    print(M[i][j], end = " ")
  print()
  
