# Default Arguments

# Default Arguments can be defined for function parameters. They are created in the function definition


def add_two_numbers(num_1=1, num_2=2):
    return num_1 + num_2

print(add_two_numbers()) # outputs 3 to the console




def add_10 (a, b = 10) :         #  IF I DONT PASS SOMETHING, JUST ASSUME ITS 10
    return a + b

print(add_10(2))        #12
print(add_10(2,100))    #102
print(add_10())         #TypeError




# `print()` and `return` ARE DIFFERENT!!
# `print()` outputs to the console
# `return` defines the value that will be received from the scope of the function


def some_func(x):
    print(x)

# is fundamentally different from
def another_func(x):
    return x





# Quick intro to f-strings
# f-strings are an easy way to interpolate a value into a string
    # defined by putting an `f` in front of quotes: `f'some text'`

"strings represens bodies of text"

"f strings allow us to put dynamic information that cant be determined during write time, only over run time"

name = "Sally"
age = 47
print(f"{name} is {age} years old")        #if i dont put the f, the {} will only be text
print( name + "is" + str{age} + "years old") #SyntaxError

# Bonus function: `input()`
# The `input()` function accepts character input from the keyboard and prints the message it is passed as a prompt.


def welcome_message(name):
    return f'Hello {name}!'

name_1 = input('Please enter your name: ')

print(welcome_message(name_1))


# Write a function that uses the `input()` function inside of it to take a user inputted number and check if that number is equal to `7`. If the number is equal to `7`, return `True`. If not, return `False`
# Hint: `input()` will return a string by default, so cast to an `int`:
   # `user_input = int(input(‘type number: ‘))`



def check_for_seven():
    user_input = int(input('type a number: '))

    if user_input == 7:
        return True
    else:
        return False


# AGAIN `print()` IS NOT `return`
# `print()` :
    # function takes the value passed into it and writes that value to the console.
# `return` :
    # Keyword used to return an object from a function        


# Variable Scope 
# Global Variables 
    # Variables defined in the main program
# Local Variables
    # Variables defined within the scope of a function
# You can access a variable declared in the global scope of the function within the local scope of a function
# If you want to change a global variable within the scope of a function, use `global var_name`

#THIS IS NOT RECOMENDED!!!!!!!! AVOID GLOBAL VARIABLES IN YOUR FUNCTION
a = 4
def my_function(b):
    return a + b





def my_function(b):
    a = 4           #This makes the variable local to the function, it doesnt belong anywhere else
    return a + b

print (my_funtion(20) )


# Define a function (give it a meaningful name) that takes two number values, and returns the modulus of the first value by the second value, multiplied by 7, then raised to the 4th power

def mod_mult_by_7_power_4(x, y):
    return ((x % y))


print(mod_mult_by_7_power_4(x=20, y=3) # --> 38416     



#Square the number

def sq_num(num):
    return(num ** 2)

print(sq_num(20))       #400


def sq_num(num):
    print(num ** 2)

print(sq_num(20))       #none



# Write a function that takes in a number between 0-999:
    # Print out whether the number is a single, double, or triple digit number. 
    # If the number is outside of that range, print a message saying that it is outside of the expected range. 

def print_num_len(num):
    if num < 0 or num > 999:
        print(f'{num} outside of expected range')
    elif num / 10 < 1: 
        print(f'{num} is single digit')
    elif num / 100 < 1:
        print(f'{num} is double digit')
    else: (f'{num} is triple digit')        # use the : after an else.

print( print_num_len(5))


#Lists are similar to array(javascript,C, C++)
#you can mix data types


my_list = [4, 6.4, "hello", 9, ["hey", "i`m a list"]]


num_lst = [4, 3, 5]
print(num_lst)
print(my_list)

#List are ordered and mutable, you can declare empty lists using  [] or list()

#Mutability can be useful


my_list = []
print(my_list)

my_list = list("hello")
print(my_list)          #breaks each letter apart


list()


# Describing a `list`
# A list is a ##collection## of arbitrary objects
# Lists are ##ordered## and ##mutable##
# Declare empty lists using `[]` or `list()`


lst_1 = []
lst_2 = list()


# Declare a list with values using [1, 2, 3]


lst_3 = [1, 2, 3]


# Lists can hold both ##scalar## types and collections


nested_list = [[2, 3, 4], [2, 1, 5]]

# `range` Function
# The `range` function helps us create a `list` of contiguous integers.
# Syntax:
    # `range(start, stop, step)`
    # Start is inclusive, stop is not
# Returns an iterator object. Need to cast this object to a list so that we can work with it at this stage.

one_to_99 = list(range(1,99+1))

range(5)            #starts at 0 goes to 4, ( five numbers)
range(5, 10)        #from 5 to 10 ( inclusive, exclusive)

n = 10
range (7, n+1 )  # 7, 8, 9, 10  (this will inculde the useal excluded(n+1))

#range(start, stop, step)


#items in a list are called elements

my_list = [55, 77, 33, "hi", 44]

#each element had a location called the index

print(my_list[3])       # hi

#local variables overite global variables


print(type(range(4, 10)))       #Class range


# `list` Indexing
# We use square brackets `[idx]` to access elements in a `list`
# Python uses ##zero-based indexing##. Therefore, we count starting from 0.
    # `lst[0]` will return the first element of the list
# List indexing also allows us to reassign the value at that index
# Lists can be unpacked into variables.


# `list` Membership
# Use the in keyword to check whether an element is in a list
    # `5 in [1, 2, 3, 4]` will be `False`
# You can conversely use not in to check if an element is not a member of the list
    # `5 not in [1, 2, 3, 4]` will be `True`


print (7 in [2, 3, 5, 7, 11] )      #boolean, if its equal to any of these, then I know I must run some special code

print ( 7 == 2, 7 == 3 )


# List Slicing
# Use list slicing if you want to access a portion of a list
    # Notation is similar to indexing, e.g. `[1:3]`
    # Syntax: `list[start:stop]`
        # The slice starts at the start value and goes up until the stop value
        # The slice will not inclued the stop value
# Like the range function, we can specify a step
    # Syntax: `list[start:stop:step]`

#Starts at 3 and goes until the lists is finished.
print (lst[3::])        #[7, 3, 3, 6, 7, 3, 6, 5]

#starts at the begining and goes to index 4(excluded), step is default positive 1
print(lst[:4:])        # [9, 8, 5, 7]

#starts at the beginning, no end specified, and steps on 4
print(lst[::4])     #[9, 3, 3]

#reverse version of your list
print(lst[::-1])        #[5, 6, 3, 7, 6, 3, 3, 7, 5, 8, 9]







    # Nested Lists
# A list that contains another list is known as a nested list
    # Example: `lst = [‘a’, ‘b’, [1, 2, 3]]`
# To access an element in a nested list, you will need two indices
    # `lst[2][0]` will access the value `1`  
# To access more than one element in a nested list, use a slice:	
    # `lst[2][:2]` will produce the slice `[1, 2]`

lst = [[7, 5, "Thing one and two"], [3, 5, 1]]        #2 elements
lst[0] #3 elements

print(lst[0][2])        #"Thing one and two"

print(lst[0][2][:6])     #Thing

lst = []
print(lst)
lst.append("Hello")
print(lst)
lst.append("World")
print(lst)


#This is different than mutation
string1 = "hello"
string2 = "world"
string1 =string1 + string2
print(string1)
print(string2)



my_obj = "hello"
print(id(my_obj))        #2086243224176

print(id(lst))


lst = []
print(id(lst))      #2086243361856
lst.append("Hello")
print(id(lst))      #2086243361856
lst.append("World")
print(id(lst))          #2086243361856



string1 = "hello"
print(id(string1))      #2086243224176
string2 = "world"
string1 =string1 + string2

print(id(string1))      #2086243455024
#we are reassigning the variable, the identifier is not pointing at it, it is now an orphan variable

print(string2)





#SHALLOW COPY
lst1 = [4, 3, 5]
lst2 = lst1

lst1.append("hello")
print(id(lst2)) #2086243519104
print(id(lst1)) #2086243519104

#pointer duplication
#both are pointing to the same object


#deep COPY
lst1 = [4, 3, 5]
lst2 = lst1.copy()
print(id(lst2)) #2086243621632
print(id(lst1)) #2086243616448



    # List Mutability
# Lists are mutable
    # The contents in a `list` can change while its `id()` stays the same.
    # Two lists that contain the same values will have different ids. 


###########################################################################################################################################
###########################################################################################################################################

---------------------------------------------------------------
# Copy a `list`
# Create a copy of a list with the `.copy()` method
    # Syntax: `lst_2 = lst.copy()`
# `list` slicing can also be used to make a copy
    # Syntax: `lst2 = lst[:]`
# It is good practice to not modify function arguments. If a function argument is a `list`, create a copy before changing that `list` in any way. 


###########################################################################################################################################
###########################################################################################################################################

---------------------------------------------------------------
# `append()` to a `list`
# The `.append()` method places a new value at the end of the `list` 
    # Syntax: `lst.append(new_item)`	
# Can append a `list` to another `list` in order to create a nested `list`.



###########################################################################################################################################
###########################################################################################################################################

---------------------------------------------------------------
# Unpacking a `list`
# We can unpack the elements of a `list` so that we are storing these elements in a variable:
    # `fruit1, fruit2, fruit3 = [‘grapes’, ‘blueberries’, ‘apples’]`
# Unpacking a `list` is untenable for a very long `list`.

# `for` loops
# For loops iterate through each element of a `list`
    # Syntax: 

#################################PRACTICE YOUR ACCUMULATOR PATTERS!!!!###################################




 
for element in list:
	print(element)

lst = [33,55, 44]

for num in lst:
    print(num)

##quare each num, then add them, sum of squares
lst = [33,55, 44, "hello", 9.4, False]
sum_of_sqrs = 0             #This is an accumulation, you might want to start it at a neutral number, or empty. 
for num in lst:
    if type(num) in [int , float]:      #This conditions make sure the input are numeric 
        sum_of_sqrs += num**2

print(sum_of_sqrs)



#Create a list of the numbers squared
lst = [33,55, 44, "hello", 9.4, False]
sqrs_lst = []             #This is an accumulation, you might want to start it at a neutral number, or empty. 
for num in lst:
    if type(num) in [int , float]:      #This conditions make sure the input are numeric 
        sqrs_lst.append(num**2)

print(sqrs_lst)


#Create a list of the numbers 
lst = [33,55, 44, "hello", 9.4, False]
num_list = []             #This is a target
for num in lst:
    if type(num) in [int , float]:      #This conditions make sure the input are numeric 
        num_list.append(num)

print(num_list)


#You can code multiple targets into one funtion
lst = [33,55, 44, "hello", 9.4, False]
num_list = []           #This is a target
sqrs_lst = []            #This is a target
for num in lst:
    if type(num) in [int , float]: 
        sqrs_lst.append(num**2)     #This conditions make sure the input are numeric 
        num_list.append(num)

print(num_list)
print(sqrs_lst)




#you can use for loops where in a problem the number of iterations is known before looping starts or it can be determined.
#you use while to iterate until it finds what you are looking for.





# Another way to use a `for` loop is to iterate through `range(len(list))` in order to access all the indices, rather than the elements themselves. 







# BREAKOUT (6 minutes)
#Given the following `list` of letters, create a function that goes through each letter and prints the letter if it is a vowel.


char_list = ['o', 'r', 'c', 'h', 'i', 'd']


# It will be helpful to write a helper function that returns True if a character is a vowel and call it within this function
# Create a plan before coding

# BREAKOUT SOLUTION


char_list = ['o', 'r', 'c', 'h', 'i', 'd']

def is_vowel(let):
    if let in ['a', 'e', 'i', 'o', 'u']:
        return True
    else:
        return False

def print_vowels(lst):
    for char in lst:
        if is_vowel(char):
            print(char)

print_vowels(char_list)


#Given two arbitrary lists, write a function that finds the common elements between them. Store these common elements in a `list`, and return that `list`

# Bonus 1: return the items sorted in the returned `list`
# Bonus 2: make sure there are no duplicates in the returned `list`

def get_common_elements(lst1, lst2):
    output = []

    for item in lst1:
        if item in lst2:
            if item not in output:
                output.append(item)
    
    return sorted(output)

lst_a = [4,9,6,5,7,8,6,2]
lst_b = [1,2,3,4,5,6,7]

print(get_common_elements(lst_a, lst_b))    #[2, 4, 5, 6, 7]

# Accumulators (are important!)
# An accumulator can be thought of as a running total that is held in a variable	
# Accumulator Pattern: 
    # Initialize the accumulator variable
    # Repeat:
        # Modify the accumulator variable
    # When the above loop terminates, the accumulator will have the correct value. 


# Sum accumulators using an `int`
# We can calculate a sum by using an integer type accumulator
summ = 0


for num in nums:
	summ += num    

# We can also calculate the sum when our list is comprised of floats. 
# The final accumulator will be a float. 



lst = [4, 3, 5, 6, 7, 2]
print( sum(lst))    

# Boolean Flags 
# Occasionally, you will need to use an accumulator that is set to a boolean value. 
# If some condition is met in the for loop, the boolean assigned to the accumulator will change to the opposite value. Otherwise, it will stay the same.
# These boolean flags can also be used as exit conditions in a loop.
# Syntax:   


accumulator = False
for element in some_list:
    # some code
    if some_condition:
        accumulator = True

# The `is_prime()` function
#This takes in a number and returns True or False


def is_prime(num):
    prime = True
    if num == 2 or num == 3:
        return True

    for divisor in range(2, num):
        if num % divisor == 0:
            prime = False
    
    return prime

for i in range(2, 100):
    print(i, is_prime(i))




def is_prime(num):
    prime = True
    if num < 2:
        prime = False

    for i in range(2, num):
        if num % i == 0:
            prime = False

    return prime

print(0, is_prime(0))  #False
print(1,is_prime(1))  #False
print(2,is_prime(2))  #True
print(3,is_prime(3))  #True
print(4,is_prime(4))   #False           
print(5,is_prime(5))  #True
print(6,is_prime(6))  #False



# `list` Accumulators
# Sometimes, you will need an accumulator that is an empty list.
# As the for loop gets evaluated, the accumulator will be appended with new values. 
# Syntax: 


accumulator = [ ]
for element in some_list:
    # some code
    accumulator.append(some_value)


# Using loops as filters
# We can filter list elements that meet a condition using accumulators.
# As the for loop is evaluated, values that meet the condition will be appended to a new empty list. 
# Syntax: 


some_list = [stuff, more_stuff]
accumulator = [ ]
for element in some_list:
    if some_condition:
        accumulator.append(element)



# `break`
# Use `break` in `for` loops to exit the loop when some condition has been met
# Syntax:


for element in some_list:
    if some_condition:
	    break

# Use `break` in `while` loops to avoid an infinite loop

# Using `break` in `is_prime()`
# Use break to exit the loop

def is_prime(num):
    prime = True
    for i in range(2, num):
        if num % i == 0:
            prime = False
            break # this will end early
    return prime


# Use `continue` in `for` loops in order to skip code and continue to the next iteration of the loop when some condition is met
# Syntax:

for element in some_list:
    if some_condition:
	    continue
    # some code


# pass
# Use pass as a placeholder for future code
# Syntax:

for element in some_list:
    pass

def function_name():
	pass



### SOMETHING is wrong!

def factorial(num):
    prod = 1
    if num == 0:
        return prod
    if num < 0:
        print('Negative factorial is undefined')

    for i in range(num+1):
        prod *= i

    return prod


print(factorial(16))



# Write a function to sum all even numbers in a `list`

numbers = (2, 5, 8, 7)

def sum_evens(num_list):
    accum = 0

    for num in num_list:
        if num % 2 == 0:
            accum += num
    return accum


print(sum_evens(numbers))   #10


lst = [44, 77, 22, 99, 33, 11]
print(sorted(lst))



# you can run bools with your sorted method
lst = [44, 77, 22, 99, False, 33, 11]
print(sorted(lst))
#[False, 11, 22, 33, 44, 77, 99]

#Change the id pointer
lst = sorted(lst)
print(lst)
#[False, 11, 22, 33, 44, 77, 99]

for i in sorted(lst, reverse = False):
    print (i)




# `max` and `min`
# `max()` returns the highest numeric value in a `list`
    # Syntax: `max(list_name)`
# `min()` returns the lowest numeric value in a `list`
    # Syntax: `min(list_name)`





lst = [44, 77, 22, 99, 33, 11]

print(min(lst))

print(max(lst))



# `any` and `all`
# A value where `bool(value) == True` can be considered ‘truthy’
# `any()` returns `True` if any of the values in a `list` are ‘truthy’
    # Syntax: a`ny(list_name)`
# `all()` returns `True` if all of the values in a `list` are ‘truthy’
    # Syntax: `all(list_name)`


lst = [44, 77, 22, 99, 33, 11]

lst = [44, 77, 22, "", [], 99, 33, 11]

#True
print(all(lst) )


#True
print(any(lst) )




# What would be the result of `len([1, 2, [1, 2]])`     #3
# What would be the result of `list(reversed([1, 5, 6, 4, 2]))`
# What do the `max` and `min` functions do?
# What is the result of `any([0, 2, 5, 6])`? What is the result of `all(['', 'a', 'c', 'p'])`
# What will be stored in the variables `lst` and `last_element` after executing the following code?
    # `lst = [1, 3, 5, 7]`
    # `last_element = lst.pop()`

len([1, 2, [1, 2]])
list(reversed([1, 5, 6, 4, 2]))


# `enumerate()`
# Sometimes you will need to write a `for` loop that can keep track of items in a `list` and their corresponding indices.
# Syntax:


for idx, num in enumerate(my_lst):
    #some code
    break

# `enumerate` needs two variables: the index gets assigned to the first variable and the item from the `list` gets assigned to the second

#One of the most useful for lists and loops

#Tuple, you can deconstruct them (unpacking) assigning multiple values at the same time
#guarantee the same number of items
#

a, b = 3, 4



lst = [44, 77, 22, 99, 33, 11]
for idx, ele, in enumerate(lst):
    print(type(tup), tup)




lst = [44, 77, 22, 99, 33, 11]
for idx, num, in enumerate(lst):
    print(num##idx)

# Create a function that will iterate over a `list` printing out each value of the `list` squared and the indexed position of each item starting at an index of `1` instead of `0`.

sample_data = [2, 4, 6, 8, 10, 12, 14]

def squared_with_indices(num_list):
    for idx, num in enumerate(num_list, 1):
        print(num**2, idx)

squared_with_indices(range(1, 20))


names = ["Jane", "Joe", "Jessie"]
ages = [32, 57, 98]

for i in range(len(ages)):
    name = names[i]
    age = ages[1]
    print(f"{name} is {age} years old")




names = ["Jane", "Joe", "Jessie"]
ages = [32, 57, 98]




#Sometimes called conditional loops, conditions exe while something is true



# While loops:
# `while`
# infinite loop
# conditional loops
# open ended problems
# menus
# `for` vs `while` loops



# `while` loops
# Use `while` loops when the number of iterations needed to complete a loop is not known
# Syntax:

"""
while some_condition:
    some code
"""

# Typically, `while` loops have some counter or flag as well. 

#for loops, boundaries of the iterations is determined, you know how many

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % 1 == 0 :
            return False

    return True

#a while loop needs to find something that meets the condition
#Find next prime number
#While n is not prime

def next_prime(n):
    while not is_prime(n+1):
        n += 1
    return n + 1 


print(next_prime(11))   #13


#Instructor likes writing loops this way

def next_prime(n):
    while True: #loop 
        n+= 1
        if is_prime(n):
            return n        #Default break


lst = []
while True:
    lst.append(input("enter a name:"))
    if input("do you want to enter another name? Y or N:") == "N":
        break


# Infinite `while` Loops
# What happens if we run the code below?
# Syntax:

```python
counter = 1
while counter < 10:
    print(‘testing’)
```

# Avoid writing infinite loops

# Using a `for` in place of a `while`
# A `for` loop can be set with an arbitrarily high ranged number and an escape condition
# Creates code safe from infinite loops


for _ in range(10000000):
    # do something
    if condition_met:
        break


# Conditional `while` Loops
# Mostly `while` loops get initialized with some sort of conditional statement. The `while` loop will execute until the statement is no longer `True`
# Syntax:


counter = 0
while some_condition:
    # some code
    # change counter
    break


# Write a function that computes and returns a `list` of all of the divisors of some positive number. Use a `while` loop. Things to think about:
    # How do you determine if a single number is a divisor of another?
    # What is your stopping condition?
    # BONUS: rewrite this with a `for` loop


def get_divisors(number):
    divisors = []
    divisor = 1

    while divisor <= number:
        if number % divisor == 0:
            divisors.append(divisor)
        divisor += 1

    return divisors

print(get_divisors(144))        #   [1, 2, 3, 4, 6, 8, 9, 12, 16, 18, 24, 36, 48, 72, 144]

## `for` loop solution


def get_divisors(number):
    divisors = []

    for divisor in range(1, number+1):
        if number % divisor == 0:
            divisors.append(divisor)

    return divisors

print(get_divisors(144))

# Menu Using a `while` Loop
# [Menu Example on Replit](https://repl.it/@gDSIprep/whileloopsmenuwhileusingaloop)


selections = []
another_order = True

while another_order == True:
    menu_string = '''Select from this list:
    1 : bread
    2 : butter
    3 : potatoes
    4 : broccoli'''

    print(menu_string)

    inp = int(input('please make a selection, 1-4: '))

    if inp in [1,2,3,4]:
        selections.append(inp)
    else:
        print('-- your selection was not understood --')
        continue

    inp2 = input('would you like to place another order? (y/n)')

    if inp2 == 'y':
        continue
    else:
        another_order = False


print(f'Your order list: {selections}')

# `for` Loops vs. `while` Loops
# In general, always use `for` loops to avoid infinite loops
    # Will always terminate at the end of an iterable when traversing elements in that iterable
    # Useful when you know how many iterations are needed
# However, there are some problems that should be solved using `while` loops
    # Open-ended problems
    # Menus
    # Run States


    # List Review BREAKOUT (3 minutes)

x = [4, 6, 1, 2, 8, 0]
print(x)
# # How would you sort your list to save it in place?
x.sort()
# or
x = sorted(x)

# # How would you sort your list to return a printed output?
print(sorted(x))

# # How would you reverse your list to save it in place?
x.reverse()
# or
x = x[::-1]
print(x)

# # What would any(x) return? all(x)?
print(any(x)) # True
print(all(x)) # False

# # How would you remove the first element in the list and append it to the end? Can you write this in a single line of code?
x = x[1:] + [x[0]]
print(x)

Would you use a for loop or a while loop?

1. Creating a letter counter based on a string
    # `for` loop
2. Trying to identify whether a dice is fair or not
    # Potentially a while loop, where eventually you wish to converge at the expected value, at which point you might use break to exit. However, you could use a for loop with many many iterations, with an exit condition.
3. Iterating over a list to identify multiples of 5
    # `for` loop
4. Creating a selection for an individual based on a given menu
    # Potentially a `while` loop, though a `for` loop with a high count could be used as instead.
5. Determine how long it might take to reach a certain threshold
    # Potentially a `while` loop, with an exit condition for when the threshold is reached. However, a `for` loop could be used instead, where the `for` loop is allowed many many iterations, with an exit condition implied by the upper bound of the iteration count.


#Write a for loop to print a menu out of this list with their number options starting at 1? Store the choices (as the item names, not the numbers) in a list. Print out the list containing the food ordered.


food_lst = [‘Pancakes’, ‘Omelet’, ‘Toast’, ‘Waffles’, ‘Bacon’, ‘Sausage’, ‘Orange Juice’]


################################################################################################################################################

---------------------------------------------------------------
# BREAKOUT SOLUTION


food_lst = [‘Pancakes’, ‘Omelet’, ‘Toast’, ‘Waffles’, ‘Bacon’, ‘Sausage’, ‘Orange Juice’]
order = []

wish_to_continue = 'Y'

while wish_to_continue == 'Y':
    print('Make a selection from this list: ')
    for idx, item in enumerate(food_lst, 1):
        print(f'{idx}: {item}')

    order.append(food_lst[int(input('Choose an item by number: ')) - 1])

    wish_to_continue = input('Choose another item? (Y/N) ')

print(order)


# Strings
# Declaring `strings`
# `string` methods
# Functions with `strings`


###############################################################################################################################

---------------------------------------------------------------
# The `string` datatype
# Strings are simply a collection of characters
# However, in Python, a `string` is a scalar type and is immutable
# Strings are declared with single, double, or triple quotes. 
    # Mostly interchangeable. Single and double quotes only work with strings that span one line. 
    # Strings that span multiple lines need to be declared using triple quotes.




"""
This 
is 
a 
string
"""

'There\'s'  #"There's"
"There's"   #"There's"

# Basic `string` Operators 
# We can use the addition operator to concatenate strings.
    # `'My first string ' + 'My second string'` => `'My first stringMy second string'`
# The multiplication operator will repeat the string `n` times. 
    # `'Repeating string' # 3` => `'Repeating stringRepeating stringRepeating string'`




name = "Carlos"
print("Hello " + name)  #Hello Carlos
print("Hello " * 2)     #Hello Hello



for c in str(4897):
    print (c / 2)       #TypeError: unsupported operand type(s) for /: 'str' and 'int'

#You cannot always cast a str to another type


print (int("44") / 2 )  #22.0

print (float("44.5") / 2 )  #22.25

print( int(float("44.5")) / 2)  #22.0







my_name = "Carlos"
my_favorite_number = 6
print(my_name + "'s favorite number is" + my_favorite_number)       #TypeError: can only concatenate str (not "int") to str


my_name = "Carlos"
my_favorite_number = 6
print(my_name + "'s favorite number is " + str(my_favorite_number))     #Carlos's favorite number is 6



#eventhough the cosion is exact, python makes all results consistent
print(40/2) #20.0
print(40/2) #20.5


# Casting to and from a `string`
# Just about any data type can be cast to a `string`.
    # Use the `string` casting function: `str()`
# Not every `string` can be cast to another data type.
    # `int('a')` will not work
# String concatenation will only work between strings
    # Need to cast any numeric variables to a `string` before concatenating. 


###############################################################################################################################

---------------------------------------------------------------
# Join a `list` to create a `string`
# Use the `join` `string` method to create a single `string` that contains all the elements of a `list`. 
    # `''.join(list)`
# All the elements of the `list` must be strings for the `join` method to work
    # You can use the `map` function to quickly cast all the elements of a `list` to strings 
    # `list(map(str, list))`


words_lst = text.split()
string_again = "".join(words_lst)
print(string_again)

#Whosewoodstheseare?IthinkIknowHishouseisinthevillagethough;HewillnotseemestoppinghereTOwatchhiswoodsfillupwithsnow.

words_lst = text.split()
string_again = "_".join(words_lst)
print(string_again)

#Whose_woods_these_are?_I_think_I_know_His_house_is_in_the_village_though;_He_will_not_see_me_stopping_here_TO_watch_his_woods_fill_up_with_snow.


#all arguments must be str type

#maps every element and get a list out where the element in that list is the result when each element in the colection is passed
#map is used to avoid getting an error, in this case, map is assuring that all elements are str type

words_lst = text.split()
words_lst.append(500000)
string_again = " ".join(map(str, words_lst))
print(string_again)

#Whose woods these are? I think I know His house is in the village though; He will not see me stopping here TO watch his woods fill up with snow. 500000


# `string` Slicing
# Use slice indexing (similar to a list) to access characters or subsequences of characters
# `string[index]`
# `string[start:end]`
# `string[start:end:skip]`



lst = [22,33,55,66,33]
print(lst[3:6:])


#Strings have indexes just like lists, but they are characters instead of words

text = """
Whose woods these are? I think I know
His house is in the village though;
He will not see me stopping here
TO watch his woods fill up with snow.
"""

print(text [7:18])      #woods these

# `string` membership
# Check if a string is a substring of another string using the in keyword. 
    # `'str' in 'string'`
    # Returns a boolean


lst = [22, 33, 55]
print(33 in lst)        #True                   

vowels = "aeiou"
c = "u"
print(c in vowels)  #True

vowels = "aeiou"
c = "aei"
print(c in vowels)  #True


#order matters
vowels = "aeiou"
c = "oei"
print(c in vowels)  #False


#print letters and their index
for idx, c in enumerate(text):
    print(idx, c)


# `replace`
# The `replace` method is used to replace every occurence of a specified substring in the original substring with another substring
    # Syntax: `string.replace(old_substring, new_substring, 1)`
# The third argument here will limit the amount of times the `replace` method will be applied to only once.


string = 'I love to look at the moon'

string = string.replace('o', 'puppy', 2)


# `enumerate`
# The `enumerate` function can be used on strings:


for idx, ch in enumerate(string):
    print(idx, ch)



#Write a function that takes a `list` like the following `list` of column names and change any spaces in the column names to underscores. Return a modified `list` with the updated names.


#column_names = ['gender', 'longest absence from school', 'is enrolled', 'enlist', 'unemployed', 'filed for bankruptcy', 'school', 'peace corps']


column_names = ['gender', 'longest absence from school', 'is enrolled', 'enlist', 'unemployed', 'filed for bankruptcy', 'school', 'peace corps']
def add_underscores(feature_list):
    new_list = feature_list.copy()
    for idx, column in enumerate(new_list):
        if ' ' in column:
            new_list[idx] = column.replace(' ', '_')
    return new_list

print(add_underscores(column_names))
#['gender', 'longest_absence_from_school', 'is_enrolled', 'enlist', 'unemployed', 'filed_for_bankruptcy', 'school', 'peace_corps']


# The `list()` Function
# A `string` can be cast to a `list` using the `list` function
    # `list(string)`
# The `list()` function will separate each character in the `string` into a new element in the returned list.


# The `split()` Method
# Quick aside: Strings are immutable so methods will not change the `string` in place like with lists. 
# This method splits a `string` at each occurrence of a specified delimiter and will return a list with each split substring.
    # `string.split(delimiter)`
# The delimiter will not be included in the returned `list`

text = """
Whose woods these are? I think I know
His house is in the village though;
He will not see me stopping here
TO watch his woods fill up with snow.
"""

sentances_lst = text.split(";")
print(sentances_lst)

#['\nWhose woods these are? I think I know\nHis house is in the village though', 
# '\nHe will not see me stopping here\nTO watch his woods fill up with snow.\n']

#Split allows us to take into a character to split on. 

word_lst = text.split()
print(word_lst)
#['Whose', 'woods', 'these', 'are?', 'I', 'think', 'I', 'know', 'His', 'house', 'is', 'in', 'the', 'village', 'though;', 'He', 'will', 'not', 'see', 'me', 'stopping', 'here', 'TO', 'watch', 'his', 'woods', 'fill', 'up', 'with', 'snow.']



word_lst = text.plit()
print(word_lst)
for word in text.split():
    print(word)







#Replace one for the other.

text = """
Whose woods these are? I think I know
His house is in the village though;
He will not see me stopping here
TO watch his woods fill up with snow.
"""
text.replace("?",".")

#'\nWhose woods these are. I think I know\nHis house is in the village though;\nHe will not see me stopping here\nTO watch his woods fill up with snow.\n'

sentances = text.replace("?",".").split(".")
print (sentances)
print(text)


#replace returns a copy, strings are immutable

# `lower()`, `upper()`, `swapcase()`, and `capitalize()`
# The `lower` method will return a `string` where all the letters are lowercase
    # Syntax: `string.lower()`
# The `upper` method will return a `string` where all the letters are uppercase
    # Syntax: `string.upper()`
# The `swapcase` method will return a `string` where all the letter’s cases are swapped
    # Syntax: `string.swapcase()`
# The `capitalize` method will return a `string` where the first letter of the `string` will be capitalized and the rest will be lower case.
    # Syntax: `string.capitalize()`


text = """
whose woods these are? I think I know.
"""
print(text)
print(text.lower()) #whose woods these are? i think i know.
print(text.capitalize())
print(text.swapcase())
print(text)


# `string` Formatting
# The `format` method will dynamically insert the variables passed in as parameters into the placeholders in a `string`
    # Syntax: `'Inserting {} into this string'.format(variable_to_insert)`
# `f` strings will dynamically insert variables into strings. The difference is that we just need to place the variable name in the curly braces.
    # Syntax: `f'Inserting {variable_to_insert} into this string'`


name = "Joanne"
age = 35
print(f"{name} is {age} years old")
#Joanne is 35 years old

name = "Joanne"
age = 35
print(f"{name} is {age} years old")

#Write a function that takes in a string. Return two parallel lists: one that contains the unique characters in the string and another that has the number of times that character appears in the original string. 

s = 'This is a string, we want you to count how many times each unique character appears in this string!'

def get_letter_count(string):
    letters = []
    counts = []

    for let1 in string:
        index = 0
        if let1 not in letters:
            letters.append(let1)
            counts.append(0)
            index = len(letters) - 1
        else:
            for idx, let2 in enumerate(letters):
                if let1 == let2:
                    index = idx
                    break
        counts[index] += 1
    return letters, counts

letters, counts = get_letter_count(s)

for i in range(len(letters)):
    print(f'{letters[i]}: {counts[i]}')


print(get_letter_count(s))


## OR ##


s = 'This is a string, we want you to count how many times each unique character appears in this string!'

def get_letter_count(string):
    letters = []
    counts = []

    for let in string:
        if let not in letters:
            letters.append(let)
            counts.append(1)
        else:
            counts[letters.index(let)] += 1
    
    return letters, counts

letters, counts = get_letter_count(s)

for i in range(len(letters)):
    print(f'{letters[i]}: {counts[i]}')



print(get_letter_count(s))


###############################################################################################################################


# `count()`
# The `count` method is used to count every occurrence of a specified substring in the original string
    # Syntax: `string.count('a')`


text = """
Whose woods these are? I think I know
His house is in the village though;
He will not see me stopping here
TO watch his woods fill up with snow.
"""
print(text.count("."))      #1
print(text.count("W"))      #1
print(text.count("FFF"))    #0
print(text.lower().count("his"))    #2


print(len(text.split()))        #30


# Applying `count()` to the letter counter


def get_letter_count(string):
    letters = []
    counts = []

    for let in string:
        if let not in letters:
            letters.append(let)
            counts.append(string.count(let))
        else:
            continue
    
    return letters, counts


print(get_letter_count(s))    


#Create a function that takes in a string. This function should split the string into a list of lowercase words that make up that string. Return a list of unique ‘cleaned’ words.
# Challenge: strip any punctuation (for now, strip commas and periods)
# Challenge: remove the common english words from the list below you are returning


remove_punct_lst =  [",", ".", ";", ":", "!", "?", "'", '"']

Remove_word_lst = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "can", "will", "just", "don", "should", "now"]

String to use: "Hello there! How are you? Why don’t you take a seat over there? Once we went to the store and we found ourselves in a strange place. We ran into two people. They were very interesting to talk to. Each of them had an interesting accent and we wondered where they were from."

def clean_string_lst(txt_in):
    punct_lst = [",", ".", ";", ":", "!", "?", "'", '"'],
    remove_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "can", "will", "just", "don", "should", "now"]

    for punct in punct_lst:
        if punct in txt_in:
            txt_in = txt_in.replace(punct, "")

    lst = []
    for word in txt_in.lower().split():
        if word not in lst + remove_words:
            lst.append(word)

    return " ".join(lst)


my_txt = "Hello there! How are you? Why don’t you take a seat over there? Once we went to the store and we found ourselves in a strange place. We ran into two people. They were very interesting to talk to. Each of them had an interesting accent and we wondered where they were from."
print( clean_string_lst(my_txt))        #TypeError: 'in <string>' requires string as left operand, not list





# Data Structures
# Sets
# Tuples
# Dictionaries


###############################################################################################################################

---------------------------------------------------------------
# The `set()` datatype
# Sets are unordered, mutable collections
# Sets will only contain unique elements
# Sets can be declared:
    # Using the set constructor `set()`
# Be careful when declaring empty sets. `{}` defaults to dictionaries.


###############################################################################################################################

---------------------------------------------------------------
# Removing Duplicates
# Sets only hold unique elements. 
    # This property is useful for removing duplicates from lists and tuples
    # Do this by casting the `list` or `tuple` to a `set`


###############################################################################################################################

---------------------------------------------------------------
# Union and Intersection
# The union and intersection methods in sets are similar to their mathematical analogues.
# The union is a set of all elements in two sets
    # Syntax: `set1.union(set2)`
# The intersection is a set of all the elements that two sets have in common
Syntax: `set1.intersection(set2)`


###############################################################################################################################

---------------------------------------------------------------
# Set Difference
# The difference of two sets A - B contains all the elements of set A that are not contained in set B
# Syntax: `set1.difference(set2)`
# `set1.difference(set2)` is different from  `set2.difference(set1)`


###############################################################################################################################

---------------------------------------------------------------
# BREAKOUT (3 minutes)

```python
l1 = [1, 4, 7, 0, 2, 5, 8]
l2 = [1, 2, 3, 4, 9]
```

# What does the intersection of these two lists return?
# What does the the union of these two lists return?
# What does the difference of `l1 - l2` return? 
# What about `l2 - l1`?


###############################################################################################################################

---------------------------------------------------------------
# BREAKOUT SOLUTION


###############################################################################################################################

---------------------------------------------------------------
# The `tuple()` datatype
# Tuples are ordered collections 
# Tuples are very similar to list with two key differences:
    # Tuples are immutable.
    # Tuples are declared using parenthesis.
# We can index and slice tuples because they are ordered
# Tuples have two methods associated with them: count and index


###############################################################################################################################

---------------------------------------------------------------
# Declaring Tuples 
# Tuples can be declared in three ways:
    # `tup = (1, 2, 3)`
    # `tup = tuple([1, 2, 3])`
    # `tup = 1, 2, 3`
# For single elements tuples:
    # `tup = (1,)`
    # `tup = tuple([1])`
    # `tup = 1,`


###############################################################################################################################

---------------------------------------------------------------
# Tuple Immutability
# Once a tuple is declared, it generally can’t be changed in anyway
    # However, if an element of a tuple is mutable, the element can be changed
# Tuples hold references to all the objects they contain, rather than the objects themselves. 


###############################################################################################################################

---------------------------------------------------------------
# BREAKOUT (4 minutes)
Write a function that has two arguments that are both tuples. Return a single tuple that is the combination of the two original tuples that skips every other element in reverse.
# Say `tuple1 = (12, 14, 16, 18)` and `tuple2 = (3, 5, 7, 9)`:
# The result would be `(9, 5, 18, 14)`

```python
def function_name(tuple1, tuple2):
   pass
```


###############################################################################################################################

---------------------------------------------------------------
# BREAKOUT SOLUTION

```python



```

###############################################################################################################################

---------------------------------------------------------------
# Dictionaries
# Dictionaries contain key/value pairs in a mutable, unordered collection.
# Keys must be immutable and unique.
# Dictionaries are declared:
    # Using curly braces `{}`
    # `dict()` constructor
# Syntax: `{key1 : value1, key2: value2, key3 : value3}`


# we dont thing of them as having an order, they also do not have indexes, they have a value key pair 

#declaring an empty dictionary
d = {}

car = {
    "make":"toyota", 
    "model":"highlander", 
    "year":"2014", 
    True: "hello",
    0: 1
    }

for k, v in car.items():
    print(v)

#toyota
#huntsman
#2014
#hello
#1


print("huntsman" in car.values())       #True

print("highlander" in car.values())     #False

print("miles" in car.keys())    #False

print("year" in car.keys())     #True

#same as code above
print("year" in car)    #True





#hashable type, takes some value, and develops a unique hash for that value, when that number is unhashed returns to that value.
#computation efficiency, confiscating info

#what makes a type hashable? if the value can change, then the value cannot be hashed. any value that you can guarantee it wont change. Immutable
#keys must be immutable and values can be anything you want

print(car)


#CRUD
#Creat Read Update Delete

#read
print(car["year"])

#create
car ["miles"] = 100_00


print(car["miles"])

#Update
car["model"] = "huntsman"
print(car["model"])     #highlander , # huntsman


#Delete the whole dictionary
del car

#Delete
del car ["miles"]
print (car)

###############################################################################################################################

---------------------------------------------------------------
# Accessing and Updating Key Value Pairs
# Access values by using the key as an index:
    # `d[key]`
    # This statement will throw an error if the key is not in the dictionary.
# Keys can be added to dictionaries by:
    # `d[new_key] = new_value`
    # Note that if the key already exists in the dictionary, this syntax will reassign the value to this new_value


###############################################################################################################################

---------------------------------------------------------------
# Dictionary Methods
# The keys method will return a list of the keys in a dictionary
    # `dct.keys()`
# The values method will return a list of the values in a dictionary
    # `dct.values()`
# The items method will return a list of tuples that contain the key/ value pairs
    # `dct.items()`


###############################################################################################################################

---------------------------------------------------------------
# Membership
# Membership for dictionaries
    # `k in dct`
    # `k in dct.keys()`
    # `v in dct.values()`


###############################################################################################################################

---------------------------------------------------------------
# Traversing a Dictionary
# Creating a for loop allows us to iterate through a dictionary’s keys

```python
for key in dictionary:
    print(key)
```

# Combining a for loop with the items method allows us to iterate through both the keys and the values of a dictionary:

```python
for key, value in dictionary.items():
    print(key, value)
```


#looping through a dictionary



###############################################################################################################################

---------------------------------------------------------------
# Deleting Key/Value Pairs
# In order to remove key/value pairs, you can use the pop method or the del keyword
    # `d.pop('some_key')`
    # `del d['some_key']`
# Create a copy of the original dictionary before changing it by adding and deleting key/value pairs
    # `dictionary.copy()`


###############################################################################################################################

---------------------------------------------------------------
# `.get()`
# To check and see if a specific key is in a dictionary, you can use the get method
    # Syntax: `dct.get(key, default=None)`

```python
states_caps_dict = {'Georgia': 'Atlanta', 'Colorado': 'Denver', 'Indiana': 'Indianapolis'}
d.get(‘Washington’, ‘Capital not found’)
```


car = {
    "make":"toyota", 
    "model":"highlander", 
    "year":"2014", 
    True: "hello",
    0: 1
    }

car.get("miles", )

car.get("year", )       #'2014'

#syntax: dct.get(key, default = None)
car.get("2014")

print(car.get("make", "key not found"))     #toyota

#if key not found, it will print the second argument you input 
print(car.get("miles", "key not found"))    #key not found





###############################################################################################################################

---------------------------------------------------------------
# Copying a dictionary

To make a copy of a dictionary you need to use the `.copy()` method
# Syntax: `dct.copy()`
# Err on the side of making copies of dictionaries
