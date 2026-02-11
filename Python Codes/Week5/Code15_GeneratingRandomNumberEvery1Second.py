# Import the random module
# Used to generate random numbers
import random

# Import the time module
# Used to create delays in the program
import time

# Start an infinite loop
# The code inside this loop runs continuously
while True:

    # Generate a random integer between 15 and 78 (inclusive)
    # Store the random number in the variable my_r
    my_r = random.randint(15, 78)

    # Print the generated random number to the console
    print(my_r)

    # Pause the program for 1 second before generating the next number
    time.sleep(1)
