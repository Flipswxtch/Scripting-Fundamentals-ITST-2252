#!/usr/bin/env python

# FILE:2252_KennedyK_Lesson3#1_GrLab.py
# NAME: Distance Calculator
# AUTHOR(s): Kevin Kennedy
# DATE: 06/29/2021
# PURPOSE: Calculate distance Brutus ran using distance = speed * time
# Print out table containing columns for hours and distance travelled at that
# hourly interval.

lineBreak = "#"*60
print(lineBreak)

print("This program will calculate the distance (in km) Brutus has run at hourly"\
"time intervals. Please answer the following prompts:")

# Get user input detailing the speed of Brutus and how long Brutus played fetch
time_spent_running = int(input("\nHow long did Brutus play fetch? Enter an "\
"integer: "))
running_speed = int(input("How fast did Brutus run? Enter an "\
"integer: "))
    
# Set up two columns to help organize data; one column
# for the hourly interval and one for the total distance ran up to that hour
print("\n\n","=" * 40,"\n Hour", "\t\t", "Brutus' Distance", "\n", "=" * 40)

# Iterate through total time spent playing using hour 1 as starting point and
# input given in time_spent_running prompt as final hour. To make sure the final 
# hour is included, add one to it. 
for hour in range(1, time_spent_running + 1):
    distance = running_speed * hour
    print("",hour, "\t\t", distance, "km")


print("\n\n\n",lineBreak)



#Keep shell window/script open:
print(input('\n\nHit Enter to Close\n'))



