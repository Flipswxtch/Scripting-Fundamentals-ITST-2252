#FILE:
#NAME:
#AUTHOR:
#DATE:
#PURPOSE:

##Group lab 1


'''distance = speed * time
As an example, Brutus ran for two hours and ran 15 kilometers per hour. So, (15 kph) * (2 hours) = 30 kilometers.
Write a program that Brutus's owner can use to track his distance. It should:
Allow Brutus's owner to input the speed of his dog
Allow Brutus's owner to input the hours Brutus was playing fetch
Loop to display the distance Brutus ran for each hour like this:
How long did Brutus play fetch? 3
How fast did Brutus run? 1'''



spacer = "#"*50


print("Welcome to the KM / Speed Brutus Calculator")

#I jacked this up will come back later
#name = input("What is the name of your dog?:")

#speed =int(input("How fast did", name,"run?"))
#time = int(input("How long did",name," play fetch in hours?"))

speed =int(input("How fast did run?"))
time = int(input("How long did play fetch in hours?"))


print(spacer)
print("Hour\tDistance in km")
for hour in range(1,time+1):
    distance = speed * hour
    print(hour,"\t", distance, "km")
print(spacer)  
    
##Group Lab 2
'''

#
##
# #
#  #
#   #
#    #
#   #
#  #
# #
##
#
'''
'''
count = 5
print("#")
for i in range(count):
    print("#", end='')
    for j in range(i):
        print(" ", end='')
    print("#")
    
for i in range(5,0,-1):
    print("#", end='')
    for j in range(i):
        print(" ", end='')
    print("#")

print("#")
'''

spaces = ' '
for numSign in range(0,1):
    print("#")
    for innerRange in range(0,4):
        print('#',spaces * innerRange, '#', sep='')
    for lowerRange in range(4,-1,-1):
        print('#',spaces * lowerRange, '#', sep='')
    print("#")
