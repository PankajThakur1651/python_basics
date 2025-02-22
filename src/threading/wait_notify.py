import threading
import queue
import time

# Shared buffer (Queue)
buffer = queue.Queue(maxsize=5)

# Producer function
def producer():
    i = 0
    while True:  # Infinite loop
        item = f"Item-{i}"
        buffer.put(item)  # Blocks if full
        print(f"Producer: Produced {item}")
        i += 1
        time.sleep(2)  # Simulate production delay

# Consumer function
def consumer():
    while True:  # Infinite loop
        item = buffer.get()  # Blocks if empty
        print(f"Consumer: Consumed {item}")
        buffer.task_done()  # Indicate processing is done
        time.sleep(2)  # Simulate processing delay

# Creating threads
producer_thread = threading.Thread(target=producer, daemon=True)
consumer_thread = threading.Thread(target=consumer, daemon=True)

# Starting threads
producer_thread.start()
consumer_thread.start()

# Let the program run for some time before stopping it
try:
    time.sleep(15)  # Run for 15 seconds
except KeyboardInterrupt:
    print("\nStopping producer and consumer.")

print("Main Thread: Exiting.")

