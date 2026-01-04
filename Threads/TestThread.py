import threading


# Creating and Starting a Thread
def print_numbers(time):
    for i in range(1, 6):
        print(f"{thread.name}, i = {i}, time = {time}")


thread = threading.Thread(target=print_numbers, args=("July 3th",))  # notice: args right inside brace has a comma

thread2 = threading.Thread(target=print_numbers, args=("July 3th",))

thread.start()
thread.join()

thread2.start()
thread2.join()


# Using Threading with a Class
class MyThread(threading.Thread):
    def run(self):
        for i in range(1, 6):
            print(i)


# Create an instance of the thread
thread = MyThread()

# Start the thread
thread.start()

# Wait for the thread to complete
thread.join()
