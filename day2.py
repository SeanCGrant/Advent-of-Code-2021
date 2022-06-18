import numpy as np

# open file and read data
fh = open('../day2_data.txt')
fData = fh.read()
fh.close()

# parse data
data = fData.split()

# split data into instruction and value lists
instructions = np.array(data[::2])
vals = np.array(data[1::2], dtype=int)

# sum each part of movement
horz = np.sum(np.where(instructions == 'forward', vals, 0))
vert = np.sum(np.where(instructions == 'down', vals, 0)) - np.sum(np.where(instructions == 'up', vals, 0))

# multiply the horizontal and vertical displacement
ans = horz * vert

print(ans)

# Part Two

# aim tracking -- create cumulative aim array
aim = np.cumsum(np.where(instructions == 'down', vals, 0)) - np.cumsum(np.where(instructions == 'up', vals, 0))

# sum each part of movement
horz = np.sum(np.where(instructions == 'forward', vals, 0))
vert = np.sum(np.where(instructions == 'forward', vals, 0) * aim)

# multiply the horizontal and vertical displacement
ans = horz * vert

print(ans)

