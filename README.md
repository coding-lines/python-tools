# python-tools
<b>An importable Python toolbox with tools for arrays, strings and simulated logic gates.</b>

Classes:
logicgates - Contains simulated AND,OR,NOT,XOR,NAND,XNOR, and NOR gates.
arrtools - Contains array operations like random arays, average array value, or array to string
strtools - Contains string operations like removing spaces, reading files in one line and writing to files in one line

Functions:

<b>logicgates:</b>

l_[THE GATE YOU WANT TO SIMULATE]([INPUT1],(depending on logical gate [INPUT2]))

example: logicgates.l_xor(1,0)

VALUES: Any integer > 0 = True
        Any integer < 0 = False
You can also input Booleans directly



<b>arrtools:</b>

arrtostr(ARRAY) 
Joins all elements of an array together.  [INPUTS: ARRAY ; OUTPUTS: STRING]

arr_avg(ARRAY)
This function will calculate the average value of all values in an array.  [INPUTS: ARRAY OF INTEGERS OR FLOATS ; OUTPUTS: AVERAGE NUMBER AS FLOAT]

arr_add(ARRAY)
This function will add up all values of an array.  [INPUTS : ARRAY OF INTEGERS OR FLOATS ; OUTPUTS: SUM AS INTEGER OR FLOAT]

arr_randint(LENGTH,FROM,TO)
This function will create an array consisting of random numbers. [INPUTS: LENGTH OF THE ARRAY AS INTEGER , LOWEST POSSIBLE RANDOM NUMBER , HIGHEST POSSIBLE RANDOM NUMBER ; OUTPUTS: ARRAY CONSISTING OF RANDOM INTEGERS.]



<b>strtools:</b>

rmspaces(STRING)
This function will remove all spaces from a string. [INPUTS: STRING ; OUTPUTS: RESULT AS STRING]

savetofile(NAME,CONTENT)
This function will save the input to a file in the current directory. [INPUTS: FILENAME AS STRING e.g ( file.txt ), FILE CONTENT ; OUTPUT: 1 ON SUCCESS , 0 ON FAIL]

readfile(NAME)
This function will read the contents of a file and return it. [INPUTS: FILENAME AS STRING e.g ( file.txt ) ; OUTPUTS: CONTENT OF THE FILE AS STRING]
