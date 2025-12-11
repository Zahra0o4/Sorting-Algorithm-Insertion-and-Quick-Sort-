import time
import os

def insertionSortWithProgress(arr, filename):
    n = len(arr)

    start_time = time.perf_counter()
    
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        # This loop breaks immediately for every single item
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        
        # We probably won't even see this print because it's too fast
        if n > 50000 and i % 50000 == 0:
            elapsed = time.perf_counter() - start_time
            percent = (i / n) * 100
            print(f"    [{filename}] Progress: {percent:.1f}%")

    end_time = time.perf_counter()
    return end_time - start_time

# DRIVER CODE
if __name__ == "__main__":
    # The FULL Ordered file list
    files_to_test = [
       "uniform-input-1000-1-float.txt",
        "uniform-input-1000-2-float.txt",
        "uniform-input-10000-1-float.txt",
        "uniform-input-10000-2-float.txt",
        "uniform-input-100000-1-float.txt",  # <--- Big one 1
        "uniform-input-100000-2-float.txt"   # <--- Big one 2
    ]
    
    results = []

    print("Starting Batch Test (BEST CASE - SORTED)...")
    print("This should be lightning fast.")
    print("=" * 60)

    for filename in files_to_test:
        if os.path.exists(filename):
            print(f"\nProcessing: {filename}...")
            
            # 1. Read the file
            with open(filename, 'r') as f:
                try:
                    arr = [float(line.strip()) for line in f if line.strip()]
                except ValueError:
                    print("Error: File contained non-numbers.")
                    continue
            
            n = len(arr)
            
            # 2. Run the Sort
            duration = insertionSortWithProgress(arr, filename)
            
            # 3. Log the result
            # using .6f precision because the numbers will be TINY
            print(f"FINISHED {filename} in {duration:.6f} seconds.")
            results.append((filename, n, duration))
            
        else:
            print(f"\nERROR: {filename} was not found.")
            results.append((filename, "MISSING", 0))

    # FINAL SUMMARY TABLE
    print("\n\n" + "="*60)
    print(f"{'FILENAME':<40} | {'SIZE':<10} | {'TIME (s)':<10}")
    print("-" * 60)
    for res in results:
        name, size, time_taken = res
        print(f"{name:<40} | {size:<10} | {time_taken:.6f}")
    print("="*60)