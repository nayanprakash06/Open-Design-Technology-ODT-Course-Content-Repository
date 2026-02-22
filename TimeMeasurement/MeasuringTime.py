import time   # Import time module to access timing functions

# Record the start time in milliseconds
# ticks_ms() returns the number of milliseconds since the ESP32 was powered on
start = time.ticks_ms()

print(start)  # Print the starting timestamp

# Loop runs from 1 to 5
for i in range(1, 6, 1):
    print(i)        # Print the current number
    time.sleep(1)   # Pause execution for 1 second (1000 milliseconds)

# Record the stop time after loop execution
stop = time.ticks_ms()

print(stop)  # Print the stopping timestamp

# Calculate the time difference safely
# ticks_diff() correctly handles timer overflow
duration = time.ticks_diff(stop, start)

# Print total execution time
print("Execution Time:", duration, "milliseconds")