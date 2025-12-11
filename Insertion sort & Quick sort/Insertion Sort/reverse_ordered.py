import time
import os

# ---------------------------------------------------------
# CORE ALGORITHM WITH PROGRESS TRACKER
# ---------------------------------------------------------
def insertionSortWithProgress(arr, filename):
    n = len(arr)
    
    # Only show the "Wait" warning for the big files
    if n > 20000:
        print(f"--> BIG FILE DETECTED ({n} items).")
        print(f"--> This will take some time (roughly 1-2 mins for 75k).")
        print("--> Do not close the window. Patience...\n")
    
    start_time = time.perf_counter()
    
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        
        # PROGRESS TRACKER:
        # Prints update every ~5000 items so you know it's alive
        if n > 20000 and i % 5000 == 0:
            elapsed = time.perf_counter() - start_time
            percent = (i / n) * 100
            print(f"    [{filename}] Progress: {percent:.1f}% ({i}/{n}) - Time: {elapsed:.0f}s")

    end_time = time.perf_counter()
    return end_time - start_time

# ---------------------------------------------------------
# DRIVER CODE
# ---------------------------------------------------------
if __name__ == "__main__":
    # The updated list of files you want to test
    files_to_test = [
        "reverse_ordered-input-1000-float.txt",
        "reverse_ordered-input-10000-float.txt",
        "reverse_ordered-input-20000-float.txt",
        "reverse_ordered-input-50000-float.txt",
        "reverse_ordered-input-75000-float.txt",
        "reverse_ordered-input-100000-float.txt"
    ]
    
    # Store results here to print a table at the end
    results = []

    print("Starting Batch Test...")
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
            print(f"FINISHED {filename} in {duration:.4f} seconds.")
            results.append((filename, n, duration))
            
        else:
            print(f"\nERROR: {filename} was not found.")
            results.append((filename, "MISSING", 0))

    # ---------------------------------------------------------
    # FINAL SUMMARY TABLE
    # ---------------------------------------------------------
    print("\n\n" + "="*60)
    print(f"{'FILENAME':<40} | {'SIZE':<10} | {'TIME (s)':<10}")
    print("-" * 60)
    for res in results:
        name, size, time_taken = res
        print(f"{name:<40} | {size:<10} | {time_taken:.4f}")
    print("="*60)