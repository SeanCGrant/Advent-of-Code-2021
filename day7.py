import numpy as np

# read data
fh = open('../day7_data.txt')
fData = fh.read()
fh.close()

# parse data
data = np.array(fData.split(','), dtype=int)

# range of possible horizontal positions
start = np.min(data)
stop = np.max(data)
positions = np.arange(start, stop+1)


# function for determining fuel cost for a given collection position
def fuel_cons(data, pos: int):
    # part 1
    #return np.sum(np.abs(data - pos))

    # part 2
    step_size = np.abs(data - pos)
    return np.sum(0.5 * step_size * (step_size+1))


# determine the fuel costs for each possible position
fuel_array = np.array([fuel_cons(data, pos) for pos in positions])

print(fuel_array)

# find the lowest fuel cost
print(np.min(fuel_array))
# and see what position that is
print(positions[np.argmin(fuel_array)])

