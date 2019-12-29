class logicgates():
    def l_and(a,b):
        return(bool(a) and bool(b))
    def l_or(a,b):
        return(bool(a) or bool(b))
    def l_not(a):
        return(not(bool(a)))
    def l_xor(a,b):
        return((bool(a) or bool(b)) and not (bool(a) and bool(b)))
    def l_nand(a,b):
        return(not(logicgates.l_and(a,b)))
    def l_xnor(a,b):
        return(not(logicgates.l_xor(a,b)))
    def l_nor(a,b):
        return(not(logicgates.l_or(a,b)))



class arraytools():

    #This function will turn your array into a string. [INPUTS: ARRAY ; OUTPUTS: STRING]
    def arrtostr(arr):
        for i in range(0,len(arr)):
            arr[i] = str(arr[i])
        return( "".join(arr))
    
    #This function will calculate the average value of all values in an array [INPUTS: ARRAY OF INTEGERS OR FLOATS ; OUTPUTS: AVERAGE NUMBER AS FLOAT]
    def array_avg(arr):
        avg_cache = 0
        try:
            for item in range(0,len(arr)):
                avg_cache = avg_cache + arr[item]
            return( avg_cache / len(arr))
            del avg_cache
        except:
            print("Data Type Error: Only run array_avg int or float arrays!")
            return(0)
        
    #This function will add up all values of an array. [INPUTS : ARRAY OF INTEGERS OR FLOATS ; OUTPUTS: SUM AS INTEGER OR FLOAT]
    def array_add(arr):
        add_cache = 0
        try:
            for item in range(0,len(arr)):
                add_cache = add_cache + arr[item]
            return( add_cache)
        except:
            print("Data Type Error: Only run array_add for int or float arrays!")
            return(0)
            
    #This function will create an array consisting of random numbers. [INPUTS: LENGTH OF THE ARRAY AS INTEGER , LOWEST POSSIBLE RANDOM NUMBER , HIGHEST POSSIBLE RANDOM NUMBER ; OUTPUTS: ARRAY CONSISTING OF RANDOM INTEGERS.]
    def array_randint(count,frm,to):
        arr_cache = []
        for item in range(0,count):
            arr_cache = arr_cache + [(__import__("random").randint(frm,to))]
        return arr_cache


class stringtools():
    
    #This function will remove all spaces from a string. [INPUTS: STRING ; OUTPUTS: RESULT AS STRING]
    def removespaces(inputstr):
        try:
            inputstr = inputstr.split(" ")
            return("".join(inputstr))
        except:
            return(inputstr)
            print("Data Type Error: You need to input a string to use the removespaces function.")

    #This function will save the input to a file [INPUTS: FILENAME AS STRING e.g ( file.txt ), FILE CONTENT ; OUTPUT: 1 ON SUCCESS , 0 ON FAIL]
    def savetofile(name,content):
        try:
            ndatei=open(name, 'w')
            ndatei.write(content)
            ndatei.close
            return(1)
        except:
            return(0)
    
    #This function will read the contents of a file and return it. [INPUTS: FILENAME AS STRING ( file.txt ) ; OUTPUTS: CONTENT OF THE FILE AS STRING]
    def readfile(name):
        with open(name,"r") as f:
            return( f.read())
            f.close()
