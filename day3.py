import numpy as np
from scipy import stats

fh = open('../day3_data.txt')
fData = fh.read()
fh.close()

# parse data
data = fData.split()
# split into 2-D array
data = np.array([[i for i in val] for val in data], dtype=int)
print(data[0])

# how many places in the binary
count = len(data[0])

# generate arrays for metrics
gamma = np.zeros(count)
epsilon = np.zeros(count)

print(len(data))

# part two extras
ox = data
co = data

# fill
for i in range(count):
    val, m = np.unique(data[:, i], return_counts=True)
    print(val)
    print(m)
    gamma[i] = val[np.argmax(m)]
    epsilon[i] = np.delete(val, np.argmax(m))

    # part two (oxygen)

    # check if last
    if len(ox) > 1:
        val, m = np.unique(ox[:, i], return_counts=True)

        # delete rows that don't conform, based on count
        # check for even count
        if (m[0] == m[1]):
            print('yes')
            ox = np.delete(ox, np.transpose(np.argwhere(ox[:, i] == 0))[0], 0)
        else:
            ox = np.delete(ox, np.transpose(np.argwhere(ox[:, i] == np.delete(val, np.argmax(m))))[0], 0)



    # (co2)
    if co.size > 1:
        val, m = np.unique(co[:, i], return_counts=True)
        if len(co) != 1:
            if (m[0] == m[1]):
                co = np.delete(co, np.transpose(np.argwhere(co[:, i] == 1))[0], 0)
            else:
                co = np.delete(co, np.transpose(np.argwhere(co[:, i] == val[np.argmax(m)]))[0], 0)


# convert from binary to decimal
# create a scalar for the binary
scalar = (np.ones(count) * 2) ** np.arange(0, count)
# convert
gamma_val = np.sum(gamma * np.flip(scalar))
eps_val = np.sum(epsilon * np.flip(scalar))

print(gamma_val * eps_val)


## Part Two

print(ox)
print(co)

ox_val = np.sum(ox * np.flip(scalar))
co_val = np.sum(co * np.flip(scalar))

print(ox_val * co_val)



