import random
import time
def insertsort(arr):
    if all(x == arr[0] for x in arr):
        return arr
    n = len(arr)
    if n == 1:
        return arr
    i = 1
    while i < n:
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
        i += 1
    return arr

def quicksort(arr):
    start_time=time.time()
    if len(arr) > 15:
        pivot = random.choice(arr)
        s = [x for x in arr if x < pivot]
        e = [x for x in arr if x == pivot]
        d = [x for x in arr if x > pivot]
        return quicksort(s) + e + quicksort(d)
    else:
        return insertsort(arr)