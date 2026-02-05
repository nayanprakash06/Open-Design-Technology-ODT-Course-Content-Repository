# FOR loop that runs a fixed number of times
# range(1, 6, 1) means:
# start = 1        → loop starts from 1
# stop  = 6        → loop stops before 6 (so last value is 5)
# step  = 1        → increase by 1 each time
for odt in range(1, 6, 1):
    # Print the current value of the loop variable 'odt'
    print(odt)

# What actually happens
# step-by-step
# 
# First loop → odt = 1 → prints 1
# 
# Second loop → odt = 2 → prints 2
# 
# Third loop → odt = 3 → prints 3
# 
# Fourth loop → odt = 4 → prints 4
# 
# Fifth loop → odt = 5 → prints 5
# 
# Loop stops before 6
