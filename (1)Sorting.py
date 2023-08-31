# import time
# import numpy.random as np
# import matplotlib.pyplot as plt

# def mergeSort(arr):
#     if len(arr) > 1:
#         r = len(arr) // 2
#         L, M = arr[:r], arr[r:]
#         mergeSort(L)
#         mergeSort(M)
#         i = j = k = 0
#         while i < len(L) and j < len(M):
#             arr[k], i, j, k = (L[i], i + 1, j, k + 1) if L[i] < M[j] else (M[j], i, j + 1, k + 1)
#         while i < len(L):
#             arr[k], i, k = L[i], i + 1, k + 1
#         while j < len(M):
#             arr[k], j, k = M[j], j + 1, k + 1

# def partition(arr, low, high):
#     pivot = arr[high]
#     i = low - 1
#     for j in range(low, high):
#         if arr[j] <= pivot:
#             i += 1
#             arr[i], arr[j] = arr[j], arr[i]
#     arr[i + 1], arr[high] = arr[high], arr[i + 1]
#     return i + 1

# def quickSort(arr, low, high):
#     if low < high:
#         pi = partition(arr, low, high)
#         quickSort(arr, low, pi - 1)
#         quickSort(arr, pi + 1, high)

# def selectionSort(arr):
#     size = len(arr)
#     for step in range(size):
#         min_idx = step
#         for i in range(step + 1, size):
#             if arr[i] < arr[min_idx]:
#                 min_idx = i
#         arr[step], arr[min_idx] = arr[min_idx], arr[step]

# def insertionSort(arr):
#     for i in range(1, len(arr)):
#         key, j = arr[i], i - 1
#         while j >= 0 and key < arr[j]:
#             arr[j + 1], j = arr[j], j - 1
#         arr[j + 1] = key

# def read_Input():
#     n = int(input("Enter the number of TV Channels: "))
#     return [int(input(f"Enter the number of viewers of Channel {i+1}: ")) for i in range(n)]

# methods = [mergeSort, quickSort, selectionSort, insertionSort]
# labels = ["Merge Sort", "Quick Sort", "Selection Sort", "Insertion Sort"]
# ch = int(input("1. Merge Sort\n2. Quick Sort\n3. Selection Sort\n4. Insertion Sort\nChoose your Algorithm: "))-1
# array = read_Input()
# method, labeldata= methods[ch], labels[ch]
# method(array)
# print('Sorted Array is:')
# print(array)

# print("******************Running Time Analysis*******************")
# elements, times = [], []
# for i in range(1, 10):
#     array = np.randint(0, 1000 * i, 1000 * i)
#     start = time.time()
#     method(array.copy())
#     end = time.time()
#     print(len(array), "Elements Sorted by", labeldata, end - start)
#     elements.append(len(array))
#     times.append(end - start)

# plt.xlabel('List Length')
# plt.ylabel('Time Complexity')
# plt.plot(elements, times, label=labeldata)
# plt.grid()
# plt.legend()
# plt.show()

import matplotlib.pyplot as plt
import time
import random


class TVChannel:
    def __init__(self, name, viewers, viewing_time):
        self.name = name
        self.viewers = viewers
        self.viewing_time = viewing_time


def create_channel(i):
    name = f"Channel (i)"
    viewers = random.randint(500, 200000)
    viewing_time = random.randint(30, 100)
    return TVChannel(name, viewers, viewing_time)


def rate_channel(channel):
    if channel.viewers >= 1500000:
        return "Rank 1-Excelent"
    elif channel.viewers >= 1000000:
        return "Rank 2- Great"
    elif channel.viewers >= 500000:
        return "Rank 3- Good"
    elif channel.viewers >= 300000:
        return "Rank 4- Average"
    elif channel.viewers >= 100000:
        return "Rank 5- Poor"
    else:
        return "Rank 6- Just shut down"


def plot_sorting_algorithms():
    sorting_algorithms = ["Merge Sort", "Quick Sort",
                          "Bubble Sort", "Selection Sort", "Insertion Sort"]
    running_times = []
    for algorithm in sorting_algorithms:
        # generate random data for sorting
        data = [random.randint(1, 1000) for _ in range(1000)]

        # Measure running time of the sorting algorithm
        start_time = time.time()

        # sort the data
        if algorithm == "Quick Sort":
            quick_sort(data)
        elif algorithm == "Insertion Sort":
            insertion_sort(data)
        elif algorithm == "Selection Sort":
            selection_sort(data)
        elif algorithm == "Merge Sort":
            merge_sort(data)
        elif algorithm == "Bubble Sort":
            bubble_sort(data)

        end_time = time.time()
        running_time = end_time - start_time
        running_times.append(running_time)

    plt.bar(sorting_algorithms, running_times)
    plt.xlabel("Sorth=ing Algorithms")
    plt.ylabel("Running Time(seconds)")
    plt.title("Running Time of Sorting Algorithms")
    plt.show()


def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = 1
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] >= key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        smaller = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(smaller) + [pivot] + quick_sort(greater)

    return quick_sort(lesser) + [pivot] + quick_sort(greater)


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        left_half = merge_sort(left_half)
        right_half = merge_sort(right_half)

        return merge(left_half, right_half)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[i])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1
    return result

# App Menu


def app_menu():
    channels = []
    while True:
        print("\nTV Channels App")
        print("1. Create 10 Channels")
        print("2. Rate Channels")
        print("3. Plot Sorting algorithms")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            for i in range(0, 10):
                channel = create_channel(i+1)
                channels.append(channel)
            print("Channels created succesfully")

        elif choice == "2":
            for channel in channels:
                rating = rate_channel(channel)
                print(
                    f"{channel.name}:\n {channel.viewers} viewers,{channel.viewing_time} hours,{rating}")
        elif choice == "3":
            plot_sorting_algorithms()
        elif choice == "4":
            print("Exiting the App...")
            break
        else:
            print("Invalid choice! PLease try again.")


# Run the app
app_menu()