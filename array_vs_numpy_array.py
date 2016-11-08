#coding:utf8

import timeit
import numpy as np

times = 10000

size = 1000
np_ary = np.array(list(range(size)))
ary = list(range(size))

def for_each_np_ary():
    ret = 0
    for v in np_ary:
        ret += v

    return ret


def for_each_ary():
    ret = 0
    for v in ary:
        ret += v

    return ret

print('Accessing array elements')
print(timeit.timeit(for_each_np_ary, number=times))
print(timeit.timeit(for_each_ary, number=times))

# time_it$ python array_vs_numpy_array.py
# 2.27572703362
# 0.504191160202

def sum_np_ary():
    return np.sum(np_ary)

def sum_ary():
    return sum(ary)

print('Sum of array elements')
print(timeit.timeit(sum_np_ary, number=times))
print(timeit.timeit(sum_ary, number=times))

# 0.0825188159943
# 0.0919990539551
