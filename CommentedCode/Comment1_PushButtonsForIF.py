# Import the Pin class from the machine module
# which is used to configure and control GPIO pins of the ESP32

# Import the module which will be used to add delays in the program

# Create an object for Push Button 1
# and configure as an INPUT. Enables the internal pull-up resistor

# Create an object for Push Button 2
# and configure as an INPUT with pull-up resistor

# Start an Infinite loop so the ESP32 keeps
# checking button states continuously
    
    # Read the current logic level of push button 1
    
    # Read the current logic level of push button 2
   
    # Check if Button 1 is pressed
    
        #if Pressed print "Only Button1 is Pressed"
    
    # Check if Button 2 is pressed
    
        #if pressed print "Only Button2 is Pressed"
    
    # Small delay for system stability (0.2 seconds) to Reduces unnecessary CPU usage
    # & Prevents messages from printing too fast