from concurrent.futures import ThreadPoolExecutor
from collections import defaultdict

shared_data = defaultdict(int)

def read_and_write(key):
    for _ in range(10):
        shared_data[key] += 1
        print(f"Key: {key}, Value: {shared_data[key]}")

if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=5) as executor:
        for i in range(5):
            executor.submit(read_and_write, i)