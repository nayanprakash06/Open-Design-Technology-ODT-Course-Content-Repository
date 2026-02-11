# Import the Pin class to work with ESP32 GPIO pins
# (Which module handles hardware pins?)

# Import time module to introduce delays

# Import the neopixel module(This module allows us to control addressable RGB LEDs)

# Create a NeoPixel object
# - Choose the GPIO pin connected to the NeoPixel data line
# - Specify the total number of LEDs in the ring
# (Think : What happens if this number is wrong?)

# Create a push button object
# - Select the GPIO pin for the button
# - Configure it as INPUT
# - Enable internal pull-up resistor

# Create a variable to keep track of the current LED index
# Start from the first LED (index 0)
# (Why not start from 1?)

# Start an infinite loop so the program keeps running
    
    # Read the current state of the push button & Store the value in a variable

    # Check if the button is pressed
        
        # Turn ON the LED at position 'i' & Set its color using RGB values
        # (What color does (255, 0, 0) represent?)
        
        # Send the updated color data to the NeoPixel strip
        # (What happens if we forget this line?)
        
        # Print the current LED index(Useful for debugging and understanding the sequence)
        
        # Move to the next LED index
    
    # Add a short delay to
    # Prevent multiple LEDs turning ON for a single press
    # Slow down execution for visibility
