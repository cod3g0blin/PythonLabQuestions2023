import threading
import time

def print_numbers():
    for i in range(1, 6):
        print(f"Thread 1: {i}")
        time.sleep(1)  # Pause the execution for 1 second

def print_letters():
    for letter in 'ABCDE':
        print(f"Thread 2: {letter}")
        time.sleep(2)  # Pause the execution for 0.5 seconds

# Create two threads
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

# Start the threads
thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()

print("Both threads have finished.")
