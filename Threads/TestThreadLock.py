import threading
import threading
from time import sleep

# Instantiate the lock correctly
my_lock = threading.Lock()


def print_numbers(name):
    for i in range(1, 6):
        # Acquire the lock
        print(f"{name} trying to acquire the lock.")
        my_lock.acquire()
        try:
            print(f"{name}: {i}")
            # do a time-consuming operation
            sleep(1)
            print(f"{name}: sleep {i}")
        finally:
            # Release the lock
            my_lock.release()
            print(f"{name} released the lock.")


def main():
    # Create threads
    thread1 = threading.Thread(target=print_numbers, args=("Thread-1",))
    thread2 = threading.Thread(target=print_numbers, args=("Thread-2",))

    # Start threads
    thread1.start()
    thread2.start()
    # Wait for threads to complete, block the calling thread
    thread1.join()
    thread2.join()


def main_two():
    # Create threads
    thread1 = threading.Thread(target=print_numbers, args=("Thread-1",))
    thread2 = threading.Thread(target=print_numbers, args=("Thread-2",))
    thread1.start()
    thread1.join()
    thread2.start()  # waiting for thread1 completed, start to execute thread2
    thread2.join()


if __name__ == "__main__":
    main_two()
