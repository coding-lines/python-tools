from cltoolbox import arrtools

print(arrtools.arr_avg(arrtools.arr_randint(1000,0,1)))
#Generates 1000 random numbers into an array and calculates the average of the 1000 values

print(arrtools.arrtostr(["Hello",","," ","World","!"]))
#Joins all of the contents of the array together

from cltoolbox import strtools

print(strtools.rmspaces("H ell      oWor l  d !"))
#Removes all spaces out of the string

print(strtools.readfile("example_commands.py"))
#Prints the content of this file

x = strtools.savetofile("hello.txt","Hello, World!")
#Saves "Hello, World!" to a file called "hello.txt"

if x==1:
    print("Saved successfully!")
else:
    print("An error occured!")

from cltoolbox import logicgates

print(int(logicgates.l_and(1,1))
#Logical AND-Gate. Returns True or 1 when both values are True or 1.

print(int(logicgates.l_xor(1,1))
#Logical XOR-Gate. Returns True or 1 when one of two values is equal to True or 1.
