import numpy as np

# read data file
fh = open('../day4_data.txt')
fData = fh.read()
fh.close()

# parse data
data = fData.split()
# grab the first line (bingo callouts)
calls = data[0]
# rest of the data
data = data[1:]
calls = calls.split(',')
calls = np.array(calls, dtype=int)

# reorganize data
boards = np.array(data, dtype=int)
boards = np.reshape(boards, (int(len(data) / 25), 5, 5))

# create called-out map
chosen = np.zeros((int(len(data) / 25), 5, 5))

score = 0

# loop through the bingo calls
for call in calls:
    # update map
    chosen = np.where(boards == call, 1, chosen)

    # check for wins
    horiz = np.sum(chosen, axis=1)
    vert = np.sum(chosen, axis=2)


    # find all horizontal wins
    win_loc = np.argwhere(horiz == 5)
    while len(win_loc) > 0:
        win_page = win_loc[0, 0]

        # if this is last winning board, break out
        if len(boards) == 1:
            # calculate score
            score = call * np.sum(np.where(chosen[win_page], 0, boards[win_page]))
            print(score)
            break

        # count the board as winning (remove from list)
        boards = np.delete(boards, win_page, axis=0)
        chosen = np.delete(chosen, win_page, axis=0)
        print('horz ' + str(win_page))
        print(len(boards))

        win_loc = np.argwhere(np.sum(chosen, axis=1) == 5)
        #break

    # now find all vertical wins
    win_loc = np.argwhere(np.sum(chosen, axis=2) == 5)
    while len(win_loc) > 0:
        win_page = win_loc[0, 0]

        # if this is last winning board, break out
        if len(boards) == 1:
            # calculate score
            score = call * np.sum(np.where(chosen[win_page], 0, boards[win_page]))
            print(score)
            break

        # count the board as winning (remove from list, and boards)
        boards = np.delete(boards, win_page, axis=0)
        chosen = np.delete(chosen, win_page, axis=0)
        print('vert ' + str(win_page))
        print(len(boards))

        win_loc = np.argwhere(np.sum(chosen, axis=2) == 5)

    # stop call loop too
    if score > 0:
        break



print(win_page)
print(boards[win_page])
print(chosen[win_page])

# calculate score
score = call * np.sum(np.where(chosen[win_page], 0, boards[win_page]))
print(score)


