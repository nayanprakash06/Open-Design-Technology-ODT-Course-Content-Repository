# Import the Pin class so we can work with GPIO pins of the ESP32
# (Ask yourself: which module handles hardware pins?)

# Import the time module

# Create a push button object
# - Choose the correct GPIO pin number
# - Configure it as an INPUT
# - Enable the internal pull-up resistor
# (Think: what value will the button give when pressed?)

# Create a variable to store the counter value & Start counting from zero
# (Think: Why should this be outside the while loop?)

# Start an infinite loop so the ESP32 keeps checking the button
    
    # Read the current state of the push button & Store the value (0 or 1) in a variable
    
    # Check if the button is pressed
    # Remember: with PULL_UP, pressed means logic LOW (0)
        
        # Increase the counter value by 1
        
        # Display the updated counter value(This helps us verify that the counter is working)
        
    # Add a small delay to Prevents multiple counts for one press & Slows down execution for readability
