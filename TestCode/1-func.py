import sys; x = 'foo'; sys.stdout.write(x + '\n')

def printme( str ):
   "This prints a passed string into this function"
   print (str)
   return;

# Now you can call printme function
printme("I'm first call to user defined function!")
printme("Again second call to the same function")

def square(x):
    y = x * x
    return y
print ("square value of 9 = " + str(square(9)))

def plus(num1: int, num2: int) -> int:
    return num1 + num2
    
def f(num1: int, my_float: float = 3.5) -> float:
    return num1 + my_float

def f(my_dict: Mapping[int, str]) -> List[int]:
    my_mapping[5] = 'maybe'  # if we try this, mypy will throw an error...
    return list(my_dict.keys())
    