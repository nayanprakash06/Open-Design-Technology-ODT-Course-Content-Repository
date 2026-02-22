Measuring Time in MicroPython using time.ticks_ms()

In MicroPython, the time.ticks_ms() function is used to measure time in milliseconds. It returns the number of milliseconds elapsed since the board was powered on.

Considering an example to calculate how long a block of code takes to execute:

1. Store the starting time using time.ticks_ms()

2. Execute the code

3. Store the ending time, again using time.ticks_ms()

4. Use time.ticks_diff(end, start) to compute the duration safely

⚠️ Always use ticks_diff() instead of direct subtraction to avoid overflow issues.

For better understanding, this folder contains one example code demonstrating this concept clearly. As an experiment, you can change the delay inside "for" loop and observe the change in time. 
