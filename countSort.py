import random
import time



def countsort(arr):

    f = [0] * (max(arr) + 1)
    for x in arr:
        f[x] += 1
    j = 0
    for x in range(len(f)):
        for i in range(f[x]):
            arr[j] = x
            j += 1
    return arr
