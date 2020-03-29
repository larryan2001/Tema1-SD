import time
import random
from countSort import countsort
from quickSort import insertsort,quicksort
from mergeSort import insertsort,interclasare,mergesort
from bubbleSort import bubbleSort
def verificareBubbleSort(arr):
    d=bubbleSort(arr)
    if d==sorted(arr):
        print("Sortare corecta")
    else:
        print("Sortare incorecta")

def verificareCountSort(arr):
    d=countsort(arr)
    if d==sorted(arr):
        print("Sortare corecta")
    else:
        print("Sortare incorecta")

def verificareQuickSort(arr):
    d=quicksort(arr)
    if d==sorted(arr):
        print("Sortare corecta")
    else:
        print("Sortare incorecta")

def verificareMergeSort(arr):
    d=mergesort(arr)
    if d==sorted(arr):
        print("Sortare corecta")
    else:
        print("Sortare incorecta")