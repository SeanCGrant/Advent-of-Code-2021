import numpy as np
import re

# read data
fh = open('../day5_data.txt')
fData = fh.read()
fh.close()

# parse data
# get list of each coordinates
x1_list = re.findall('(\d+),\d+ -> \d+,\d+', fData)
y1_list = re.findall('\d+,(\d+) -> \d+,\d+', fData)
x2_list = re.findall('\d+,\d+ -> (\d+),\d+', fData)
y2_list = re.findall('\d+,\d+ -> \d+,(\d+)', fData)
# create full array
coords = np.array([x1_list, y1_list, x2_list, y2_list], dtype='int')
print(coords[:, :5])

# create grid
sea_map = np.zeros((np.max([np.max(coords[0]), np.max(coords[2])]) + 2, np.max([np.max(coords[1]), np.max(coords[3])]) + 2))

# fill grid

# do for loop for now -- look to improve later?
for wall in range(coords.shape[1]):
    x1, y1, x2, y2 = coords[:, wall]

    if x1 == x2:
        # horizontal line
        ymin, ymax = min(y1, y2), max(y1, y2)
        # increase map line by 1
        sea_map[x1, ymin:ymax+1] = sea_map[x1, ymin:ymax+1] + 1

    elif y1 == y2:
        # vertical line
        xmin, xmax = min(x1, x2), max(x1, x2)
        # increase map line by 1
        sea_map[xmin:xmax+1, y1] = sea_map[xmin:xmax+1, y1] + 1

    else:
        # diagonal line
        if x2 > x1:
            x_inc = 1
        else:
            x_inc = -1

        if y2 > y1:
            y_inc = 1
        else:
            y_inc = -1

        while x1 != x2:
            sea_map[x1, y1] += 1
            x1 += x_inc
            y1 += y_inc

        sea_map[x1, y1] += 1


# check for overlapping lines (a value of 2 or more in the map)
sea_check = sea_map >= 2

# count the number of instances
count = np.sum(sea_check)

print(count)


a = np.random.random((3,5))
print(a)
print(a[::2, 1::2])

