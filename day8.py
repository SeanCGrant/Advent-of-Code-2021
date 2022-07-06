import numpy as np
import re

# read data
fh = open('../day8_data.txt')
fData = fh.read()
fh.close()

# parse data
data = fData.split('\n')
data = list(map(lambda x: re.split('[\s]', x), data[:-1]))
# list of possible outputs, followed by list of four digits
data_sorted = [[outputs[:10], outputs[11:]] for outputs in data]
data_sorted = np.array(data_sorted, dtype=object)

# Part 1
# count digits that match condition (length of 2, 3, 4, or 7)
# get lengths
digit_len = np.array(list(map(lambda x: [len(digit) for digit in x[1]], data_sorted)), dtype=int)
list_len = np.array(list(map(lambda x: [len(digit) for digit in x[0]], data_sorted)), dtype=int)
# find where they lengths match
digit_check = np.where(((digit_len == 2) | (digit_len == 3) | (digit_len == 4) | (digit_len == 7)), 1, 0)

# print answer (sum of matches)
print(np.sum(digit_check))


# Part 2 #

tot = 0
alph_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
number_dict = {'abcefg': 0, 'cf': 1, 'acdeg': 2, 'acdfg': 3, 'bcdf': 4, 'abdfg': 5,
               'abdefg': 6, 'acf': 7, 'abcdefg': 8, 'abcdfg': 9}

for j, display in enumerate(data_sorted):
    full_list = display[0]
    # track the number of times each letter appears, starting from 'a'
    let_count = np.zeros(10)

    for i, alph in enumerate(alph_list):
        let_count[i] = sum([1 if alph in x else 0 for x in full_list])

    # find unique count letters first ('b' == 6, 'e' == 4, 'f' == 9)
    b = alph_list[np.argwhere(let_count == 6)[0, 0]]
    e = alph_list[np.argwhere(let_count == 4)[0, 0]]
    f = alph_list[np.argwhere(let_count == 9)[0, 0]]

    # work out other letters
    c = full_list[np.argwhere(list_len[j] == 2)[0, 0]].replace(f, '')
    a = full_list[np.argwhere(list_len[j] == 3)[0, 0]].replace(c, '').replace(f, '')
    d = full_list[np.argwhere(list_len[j] == 4)[0, 0]].replace(b, '').replace(c, '').replace(f, '')

    # g is the leftover
    g = 'abcdefg'.replace(a, '').replace(b, '').replace(c, '').replace(d, '').replace(e, '').replace(f, '')

    # make a string to use in translation
    current_order = a+b+c+d+e+f+g

    # translate back to origin pattern and then sum
    tot += 1000 * number_dict[''.join(sorted(display[1][0].translate(display[1][0].maketrans(current_order, 'abcdefg'))))]
    tot += 100 * number_dict[
        ''.join(sorted(display[1][1].translate(display[1][0].maketrans(current_order, 'abcdefg'))))]
    tot += 10 * number_dict[
        ''.join(sorted(display[1][2].translate(display[1][0].maketrans(current_order, 'abcdefg'))))]
    tot += 1 * number_dict[
        ''.join(sorted(display[1][3].translate(display[1][0].maketrans(current_order, 'abcdefg'))))]


# answer
print(tot)



