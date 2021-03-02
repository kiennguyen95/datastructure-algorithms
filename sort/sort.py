def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def selectionSort(arr):
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


def insertionSort(arr):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
    return arr


def mergeSort(arr, left = None, right = None):
    left = 0 if left is None else left
    right = len(arr) - 1 if right is None else right
    if left < right:
        mid = (left + right) // 2
        mergeSort(arr, left, mid)
        mergeSort(arr, mid + 1, right)
        merge(arr, left, mid, right)
    return arr


def merge(arr, left, mid, right):
    L = arr[left:mid + 1]
    R = arr[mid + 1:right + 1]
    i = j = 0
    k = left
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1


import unittest


class TestSort(unittest.TestCase):
    input = [
        [],
        [1],
        [2, 2, 2],
        [1, 0, 2, 3, 5, 4],
        [0, -2, 3, 3, -5],
    ]
    def testBubbleSort(self):
        for arr in self.input:
            self.assertEqual(bubbleSort(arr), sorted(arr))

    def testSelectionSort(self):
        for arr in self.input:
            self.assertEqual(selectionSort(arr), sorted(arr))

    def testInsertionSort(self):
        for arr in self.input:
            self.assertEqual(insertionSort(arr), sorted(arr))

    def testMergeSort(self):
        for arr in self.input:
            self.assertEqual(mergeSort(arr), sorted(arr))


if __name__ == '__main__':
    unittest.main(verbosity=2)
