import numpy as np

# read data
fh = open('../day9_data.txt')
fData = fh.read()
fh.close()

# parse data
data = fData.split()
col_count = len(data[0])
data_arr = np.array(list(map(lambda x: list(x), data)), dtype=int)

# find low points
# map differences
adj_mat = -1 * np.ones((data_arr.shape[0], data_arr.shape[1], 4))
# differenc from above
adj_mat[1:, :, 0] = data_arr[1:, :] - data_arr[:-1, :]
# from below
adj_mat[:-1, :, 1] = data_arr[:-1, :] - data_arr[1:, :]
# from left
adj_mat[:, 1:, 2] = data_arr[:, 1:] - data_arr[:, :-1]
# from right
adj_mat[:, :-1, 3] = data_arr[:, :-1] - data_arr[:, 1:]

# locate all of the low points (differences all less than 0); add 1, and set all others to 0
selection = np.where(((adj_mat[:, :, 0] < 0) & (adj_mat[:, :, 1] < 0) &
                       (adj_mat[:, :, 2] < 0) & (adj_mat[:, :, 3] < 0)), data_arr + 1, 0)
# sum the result
ans = np.sum(np.where(((adj_mat[:, :, 0] < 0) & (adj_mat[:, :, 1] < 0) &
                       (adj_mat[:, :, 2] < 0) & (adj_mat[:, :, 3] < 0)), data_arr + 1, 0))


# Part 2

np.where(adj_mat[:, :, 0])

# find the direction each element will go
dir_mat = np.apply_along_axis(np.argmax, 2, adj_mat)
# give the low points a value of -1
dir_mat = np.where(((adj_mat[:, :, 0] < 0) & (adj_mat[:, :, 1] < 0) &
                    (adj_mat[:, :, 2] < 0) & (adj_mat[:, :, 3] < 0)), -1, dir_mat)


# iterate to convergence #
# starting dummy array for "old" map
old_map = np.ones(data_arr.shape)
# start the map by giving weight 1 to all tiles except those with a "9", which get a weight of 0
new_map = np.where(data_arr == 9, 0, np.ones(data_arr.shape))

while (not np.array_equal(old_map, new_map)):

    old_map = new_map

    # tiles that want to stay (low points)
    new_map = np.where(dir_mat == -1, old_map, 0)
    # tiles that move up
    new_map[:-1, :] += np.where((dir_mat[1:, :] == 0), old_map[1:, :], 0)
    # tiles that move down
    new_map[1:, :] += np.where((dir_mat[:-1, :] == 1), old_map[:-1, :], 0)
    # tiles that move left
    new_map[:, :-1] += np.where((dir_mat[:, 1:] == 2), old_map[:, 1:], 0)
    # tiles that move right
    new_map[:, 1:] += np.where((dir_mat[:, :-1] == 3), old_map[:, :-1], 0)

# return three highest values
highest_vals = np.flip(np.sort(new_map.ravel()[np.flatnonzero(new_map)]))[:3]
# multiply them together
ans = np.prod(highest_vals)



print(ans)


