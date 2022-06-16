import numpy as np

# read data
fh = open('../day1_data.txt')
fData = fh.read()
fh.close()

# parse data
fData = fData.split('\n')
data = np.array(fData[:-1], dtype=int)
shift_data = np.roll(data, -1)


#check_inc = shift_data[:-1] > data[:-1]
check_inc = data[1:] > data[:-1]
total = np.sum(check_inc)

print(total)

print(data[:20])
print(shift_data[:20])
print(check_inc[:20])
total = np.sum(check_inc[:20])
print(total)

# part 2

cum_data = data.cumsum()

sum_window = cum_data[2:]
sum_window[1:] = cum_data[3:] - cum_data[:-3]
check_cum_inc = sum_window[1:] > sum_window[:-1]

print(sum_window[:5])
print(np.sum(check_cum_inc))


