import time
import random

def partition(arr, low, high):
    # random pivot so reverse inputs don't crash
    pivot_index = random.randint(low, high)
    swap(arr, pivot_index, high)
    pivot = arr[high]

    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            swap(arr, i, j)

    swap(arr, i + 1, high)
    return i + 1

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def quickSort(arr, low, high):
    # optimized quicksort without deep recursion
    while low < high:
        pi = partition(arr, low, high)
        if (pi - low) < (high - pi):
            quickSort(arr, low, pi - 1)
            low = pi + 1
        else:
            quickSort(arr, pi + 1, high)
            high = pi - 1

def load_floats_from_file(filename):
    with open(filename, "r") as f:
        return [float(x.strip()) for x in f if x.strip() != ""]

files = [
     "uniform-input-1000-1-float.txt",
        "uniform-input-1000-2-float.txt",
        "uniform-input-10000-1-float.txt",
        "uniform-input-10000-2-float.txt",
        "uniform-input-100000-1-float.txt",
        "uniform-input-100000-2-float.txt"
]

if __name__ == "__main__":
    results = []

    for file in files:
        arr = load_floats_from_file(file)

        start = time.time()
        quickSort(arr, 0, len(arr) - 1)
        end = time.time()

        runtime = end - start
        results.append((file, runtime))

    # print table
    print("\n============================================")
    print("                 RUNTIME TABLE              ")
    print("============================================")
    print(f"{'File Name':40} | {'Time (seconds)'}")
    print("--------------------------------------------")
    for file, t in results:
        print(f"{file:40} | {t:.6f}")
    print("============================================")
