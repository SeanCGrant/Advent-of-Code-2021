import numpy as np
from scipy.linalg import toeplitz

# read data
fh = open('../day6_data.txt')
fData = fh.read()
fh.close()

# parse data
data = fData.split(',')
data = np.array(data, dtype=int)

# provided info
days = 80  # part 1
days = 256 # part 2

# Create a transfer matrix
row = np.array([0,0,0,0,0,0,0,0,1])
col = np.array([0,1,0,0,0,0,0,0,0])
mat = toeplitz(col, row)
mat[0, 6] = 1

# count starting fish lifespans
values, counts = np.unique(data, return_counts=True)
counts = [counts[np.argwhere(values == i)[0, 0]] if i in values else 0 for i in range(9)]

print(values)
print(counts)

# raise the transfer matrix to the number of days
mat = np.linalg.matrix_power(mat, days)
# multiply the starting count array by this matrix
final_counts = np.matmul(counts, mat)
# sum the results
total = np.sum(final_counts)

print(final_counts)
print(total)


