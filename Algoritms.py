import Masiv
import sys

sys.setrecursionlimit(10000)
blok = Masiv.blok

#Bubble sort
def bubble_sort(blok):
    arr = blok[:]
    for i in range(0, len(arr)):
        for j in range(0, len(arr) - i - 1):
            if (arr[j] > arr[j + 1]):
                temp = arr[j]
                arr[j] , arr[j + 1] = arr[j + 1] , arr[j]
    return arr

# Selection sort
def selection_sort(blok):
    arr = blok[:]
    for i in range(len(arr)):
        temp = i
        for j in range(i + 1, len(arr)):
            if (arr[temp] > arr[j]):
                temp = j
        (arr[i], arr[temp]) = (arr[temp], arr[i])
    return arr

# Shuffle sort
def shuffle_sort(blok):
    arr = blok[:]
    Swaped = True
    left = 0
    right = len(arr) - 1
    while (Swaped == True):
        Swaped = False
        for i in range(left, right):
            if (arr[i] > arr[i + 1]):
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                Swaped = True
        right -= 1
        if (not(Swaped)):
            break
        Swaped = False
        for i in range(right, left, -1):
            if (arr[i] < arr[i - 1]):
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                Swaped = True          
        left += 1
    return arr

# Shell sort
def shell_sort(blok):
    arr = blok[:]
    n = len(arr)
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = arr[i]
            j = i
            while (j >= interval) and (arr[j - interval] > temp):
                arr[j] = arr[j - interval]
                j -= interval
            arr[j] = temp
        interval //= 2
    return arr

# Quick sort
def quick_sort (blok):
    arr = blok[:]
    if len(arr) <= 1:
        return arr
    else:
        pivot = (arr[0])
        left = [x for x in arr[1:] if x < pivot]
        right = [x for x in arr[1:] if x >= pivot]
        return quick_sort(left) + [pivot] + quick_sort(right);

# Merge sort
def merge_sort (blok):
    arr = blok[:]
    n = len(arr)
    if n > 1:
        mid = (n // 2)
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    return arr