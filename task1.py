import threading

def print_numbers():
    for i in range(1, 11):
        print(i)

def print_squares():
    for i in range(1, 11):
        print(i * i)

if __name__ == "__main__":
    thread1 = threading.Thread(target=print_numbers)
    thread2 = threading.Thread(target=print_squares)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()