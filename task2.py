import threading

counter = 0
lock = threading.Lock()

def increment_counter():
    global counter
    for _ in range(100):
        with lock:
            counter += 1

if __name__ == "__main__":
    threads = []
    for _ in range(3):
        thread = threading.Thread(target=increment_counter)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("Final counter value:", counter)  # Should be 300