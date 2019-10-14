#!/usr/bin/env python
# coding: utf-8

# In[1]:


#-*- coding: utf-8 -*-


# <img align="right" style="max-width: 200px; height: auto" src="hsg_logo.png">
# 
# ###  Lab 02 - "Introduction to Python Programming II"
# 
# Introduction to ML and DL, University of St. Gallen, Autumn Term 2019

# The lab environment of the **"Introduction to Machine Learning and Deep Learning"** lecture is powered by Jupyter Notebooks (https://jupyter.org), which allow one to perform a great deal of data analysis and statistical validation. In this second lab, we want to have a look at the basic data types, containers, decision structures, loops and functions of the Python programming language.

# The second lab (**'Halloween Edition'**) builds in parts on the excellent Python tutorial of the Stanford University CS 231n lecture series developed by Andrej Karpathy, Justin Johnson and Fei-Fei Li. The original tutorial is available under the following URL: http://cs231n.github.io/python-numpy-tutorial/. 
# 
# In case you experiencing any difficulties with the lab content or have any questions pls. don't hesitate to contact Marco Schreyer (marco.schreyer@unisg.ch).

# ### Lab Objectives:

# After today's lab you should be able to:
#     
# > 1. Understand the basic **data types** of the Python e.g. integer, boolean, string.
# > 2. Understand the basic **data containers** of Python e.g. lists and dictionaries.
# > 3. Know Python's **decision structures** to guide the worklow of a program.
# > 4. Understand how to **loop** over data containers in order to access and manipulate individual values.
# > 5. Implement small **functions** that allow for the execution of several Python statements.

# ### Let's start with a motivational video:

# In[2]:


from IPython.display import YouTubeVideo
# Powered by TensorFlow: helping paleographers transcribe medieval text using machine learning
YouTubeVideo('v-FgOACRgfs', width=1000, height=600)


# ### 1. Python Versions

# There are currently two different supported versions of Python, 2.x and 3.x. 
# 
# Somewhat confusingly, Python 3.x introduced many backwards-incompatible changes to the language, so code written for 2.x may not work under 3.x and vice versa. For this class, all code will use Python 3.x (were x referes to an arbitrary version number).

# You may want to check your Python version at the command line by running python **--version**.

# ### 2. Fundamental Python Data Types

# In general, a data type define the format, sets the upper and lower bounds of the data so that a program could use it appropriately. However, **Python data types** are just more than that. In Python, we don’t need to declare a variable with explicitly mentioning the data type. This feature is famously known as **dynamic typing**.

# Python determines the type of a literal directly from the syntax at **runtime**. For example, the quotes mark the declaration of a string value, square brackets represent a list and curly brackets for a dictionary. Also, the non-decimal numbers will get assigned to Integer type whereas the ones with a decimal point will be a float.

# There are four basic data types in the Python programming language:
# 
# > * **Integer's** - represent positive or negative whole numbers with no decimal point.
# > * **Float's** - represent positive or negative real numbers and are written with a decimal point.
# > * **String's** - represent sequences of unicode characters.
# > * **Boolean's** - represent constant objects that are either 'False' and 'True'. 

# #### 2.1 Numerical Data Type "integer"

# Numbers are one of the most prominent Python data types. Numbers in Python are often called just **integers** or **'ints'**, and are positive or negative whole numbers with no decimal point. In Python 3, there is effectively no limit to how long an integer value can be. 
# 
# Of course, it is constrained by the **amount of memory** your system has, as are all things. But beyond that, an integer can be as long as you need it to be:

# In[42]:


x = 3
x


# Print the variable type:

# In[43]:


type(x)


# Basic mathematical operations:

# In[44]:


print(x + 1)   # addition
print(x - 1)   # subtraction
print(x * 2)   # multiplication
print(x ** 2)  # exponentiation 


# Basic mathematical operations (shortcuts):

# In[45]:


x += 1
print(x)  # prints "4"
x *= 2
print(x)  # prints "8"


# #### 2.2 Numerical Data Type "float"

# The **float** type in Python represents real numbers and are written with a decimal point dividing the integer and fractional parts. As result, float values are specified with a decimal point and are often called just **'floats'**.
# 
# A float type number can have precision up to **15 decimal places**:

# In[46]:


y = 3.0
print(y)


# Print the variable type:

# In[47]:


type(y)


# Basic mathematical operations:

# In[48]:


print(y + 1)   # addition
print(y - 1)   # subtraction
print(y * 2)   # multiplication
print(y ** 2)  # exponentation


# Optionally, the character e or E followed by a positive or negative integer may be appended to specify scientific notation:

# In[49]:


z = 1e-7      # equals 0.0000001
print(z)
print(z + 1)
print(z * 2)
print(z ** 2)


# #### 2.3 Non-Numerical Data Type "string"

# A sequence of one or more characters enclosed within either single quotes **‘** or double quotes **”** is considered as **string** in Python. Any letter, a number or a symbol could be a part of the sting. All the characters between the opening delimiter and matching closing delimiter are part of the string:

# In[50]:


hello = 'hello'   # string literals can use single quotes
world = "world, my name is peterli"   # or double quotes; it does not matter.
print(hello)


# Print the variable type:

# In[51]:


type(hello)


# Print the length of each string in terms of a number of characters:

# In[52]:


print(len(hello))
print(len(world))


# Like the most programming languages, Python allows to access individual characters of a string. But it also supports negative indexes. Index of `‘-1’` represents the last character of the String. Similarly using `‘-2’`, we can access the penultimate character of the string and so on:

# In[53]:


halloween = 'spooky'
halloween[0]   # get the first string character


# In[54]:


print(halloween[-1])    # get the last string character
print(halloween[-2])    # get the penultimate character


# Concatenate two strings, e.g., to form a sentence:

# In[55]:


hw = hello + '_' + world + ' 12' # string concatenation
print(hw)  # prints "hello world, my name is peterli 12"


# Concatenate two strings in C/C# notation (also allowed in Python):

# In[56]:


hw2 = ' %s %s %d' % (hello, world, 12)  # sprintf style string formatting
print(hw2)  # prints "hello world, my name is hubert 12"


# Concatenate two strings in Python3 notation:

# In[57]:


hw3 = '{} {} 12'.format(hello, world)
print(hw3) # prints "hello world, my name is hubert 12"


# String objects have a bunch of useful methods; for example:

# In[58]:


s = "hello"                     # init string variable
print(s.capitalize())           # capitalize a string; prints "Hello"
print(s.upper())                # convert a string to uppercase; prints "HELLO"
print(s.rjust(7))               # right-justify a string, padding with spaces; prints "  hello"
print(s.center(7))              # center a string, padding with spaces; prints " hello "
print(s.replace('l', '(ell)'))  # replace all instances of one substring with another;
                                # prints "he(ell)(ell)o"
print('  world '.strip())       # strip leading and trailing whitespace; prints "world"


# #### 2.4 Non-Numerical Data Type "boolean"

# Python 3 provides a Boolean data type. Objects of type boolean type may have one of two values, "True" or "False":

# In[59]:


a = True
b = False
print(a)
print(b)


# Print the variable type:

# In[60]:


type(a)


# Booleans are often used in Python to test conditions or constraints. For example, a string in Python can be tested for truth value. The return type will be then a Boolean value (True or False). Let’s have a look at a few examples:

# In[61]:


s1 = 'Scary Halloween'
result_upper = s1.isupper()        # test if string contains only upper case characters
print(result_upper)


# Let's have a look at a couple more examples:

# In[62]:


s2 = 'SCARY HALLOWEEN'
result_upper = s2.isupper()        # test if string contains only upper case characters
print(result_upper)


# In[63]:


n1 = 10
result_greather_than = n1 > 100                 # test if 10 > 100
print(result_greather_than)


# In[64]:


n2 = 99
result_in_between = n2 > 10 and n2 < 100        # test if 99 > 10 and 99 < 100
print(result_in_between)


# We can even logically combine the tested conditions above:

# In[65]:


print(a and b)               # Logical AND; prints "False"
print(a or b)                # Logical OR; prints "True"
print(a and result_upper)    # Logical AND; prints "True"
print(not a)                 # Logical NOT; prints "False"
print(a != b)                # Logical XOR; prints "True"


# As you will see in upcoming labs, expressions in Python are often evaluated in Boolean context, meaning they are interpreted to represent truth or falsehood. A value that is true in Boolean context is sometimes said to be “truthy,” and one that is false in Boolean context is said to be “falsy”.

# ### Exercises:

# We recommend you to try the following exercises as part of the lab:
# 
# **1. Write a set of (or single) Python command(s) that compare the first and last character of a string.**
# 
# > Write a set of Python commands that compare the first and last character of a string. In case both characters are the same print 'True' otherwise print 'False'. Test your statements using the words 'spooky' and 'sweets'. 

# In[ ]:





# **2. Write a set of (or single) Python command(s) that determine the properties of a string.**
# 
# > Write a set of Python commands that determine the number of characters of a string and if the characters are all upper case. If the number of characters is between 5 and 12 characters and all upper case print 'True' otherwise print 'False'. Test your statements using the words 'BROOMSTICK', 'ghostly', and 'mYstEriOUs'.

# In[ ]:





# **3. Write a set of (or single) Python command(s) that prints a very scary sentence.**
# 
# > Write a set of Python commands that prints the most scary sentence that you could imagine. The sentence should include at least 3 of the following words 'tarantula', 'moonlight', 'supernatural', 'fog', 'owl', 'nightmare', or 'poltergeist'. 

# In[ ]:





# ### 3. Fundamental Python Data Containers

# There are four collection data types in the Python programming language:
# 
# > * **List** - is a collection which is ordered and changeable. Allows duplicate members.
# > * **Tuple** - is a collection which is ordered and unchangeable. Allows duplicate members.
# > * **Set** - is a collection which is unordered and unindexed. No duplicate members.
# > * **Dictionary** - is a collection which is unordered, changeable and indexed. No duplicate members.
# 
# When choosing a collection type, it is useful to understand the properties of that type. Choosing the right type for a particular data set could mean retention of meaning, and, it could mean an increase in efficiency or security. 
# 
# During this lab, we will have a closer look into **lists** and **dictionaries**.

# #### 3.1. Data Container "List"

# A list is a collection of basic Python data types "elements" which is ordered and changeable. In Python, lists are written with square brackets (equivalent to an array). Python lists allow duplicate elements, are resizeable and can contain elements of different data types. Lists can be used like this:

# In[66]:


spooky_list = [3, 1, 2, 5, 9]    # create a list
print(spooky_list)               # print list


# Print the variable type:

# In[67]:


type(spooky_list)


# Determine indvidual elements of a list:

# In[68]:


print(spooky_list[2])           # print third element of list created
print(spooky_list[-1])          # print the last list element


# Determine number of list elements:

# In[69]:


print(len(spooky_list))         # print the number of elements contained in the list


# Replace a list element by assigning a new value at a specific index:

# In[70]:


spooky_list[2] = 'happy'        # lists can contain elements of different types
print(spooky_list)


# Append an element to the end of a list:

# In[71]:


spooky_list.append('coding')    # add a new element to the end of the list
print(spooky_list)


# Remove the last element of a list:

# In[72]:


this_last = spooky_list.pop()   # remove and return the last element of the list
print(this_last)                # prints the element removed 
print(spooky_list)              # prints the remaining elements


# Create a list of numbers:

# In[73]:


list_of_scary_numbers = list(range(5))     # range is a built-in function that creates a list of integers
print(list_of_scary_numbers)               # prints "[0, 1, 2, 3, 4]"


# Slice list using distinct indexing techniques:

# In[74]:


print(list_of_scary_numbers[2:4])    # get a slice from index 2 to 4 (exclusive); prints "[2, 3]"
print(list_of_scary_numbers[2:])     # get a slice from index 2 to the end; prints "[2, 3, 4]"
print(list_of_scary_numbers[:2])     # get a slice from the start to index 2 (exclusive); prints "[0, 1]"
print(list_of_scary_numbers[:])      # get a slice of the whole list; prints ["0, 1, 2, 3, 4]"
print(list_of_scary_numbers[:-1])    # slice indices can be negative; prints ["0, 1, 2, 3]"


# Replace range of list elements:

# In[75]:


list_of_scary_numbers[2:4] = [8, 9]  # assign a new sublist to a slice
print(list_of_scary_numbers)         # prints "[0, 1, 8, 9, 4]"


# #### 3.2. Data Container "Dictionary"

# In Python, dictionaries are used to stores (key, value) pairs. A dictionary is a collection of basic Python data types "elemets" which is unordered, changeable and indexed. In Python, dictionaries are written with curly brackets. Dictionaries can be used like this:

# In[76]:


this_screaming_dictionary = {'cat': 'spooky', 'night': 'scary'}  # create a new dictionary
print(this_screaming_dictionary)


# Retrieve and print the value corresponding to the key "cat":

# In[77]:


print(this_screaming_dictionary['cat'])          # get an entry from a dictionary; prints "spooky"


# Add a new dictionary element:

# In[78]:


this_screaming_dictionary['pumpkin'] = 'ugly'    # set an entry in a dictionary
print(this_screaming_dictionary)


# Retrieve and print the value corresponding to the added entry with key "pumpkin":

# In[79]:


print(this_screaming_dictionary['pumpkin'])          # get an entry from a dictionary; prints "ugly"


# Retrieve and print all dictionary keys:

# In[80]:


keys = this_screaming_dictionary.keys()          # obtain all dictionary keys
print(keys)


# Retrieve and print all dictionary values:

# In[81]:


values = this_screaming_dictionary.values()      # obtain all dictionary values
print(values)


# Try to retrieve a dictionary value that is not contained in the dictionary (this will result in an error): 

# In[82]:


#print(this_dictionary['ghost'])                  # KeyError: 'ghost' not a key of the dictionary


# However, we can "catch" such erros using:  

# In[83]:


print(this_screaming_dictionary.get('ghost', 'N/A'))       # get an element with a default; prints "N/A"
print(this_screaming_dictionary.get('pumpkin', 'N/A'))     # get an element with a default; prints "ugly")


# Remove an element from a dictionary:

# In[84]:


del this_screaming_dictionary['pumpkin']                   # remove an element from a dictionary
print(this_screaming_dictionary)


# Try to retrieve the removed dictionary element:

# In[85]:


print(this_screaming_dictionary.get('pumpkin', 'N/A'))    # "pumpkin" is no longer a key; prints "N/A"


# ### Exercises:

# We recommend you to try the following exercises as part of the lab:
# 
# **1. Write a set of (or single) Python command(s) that determine the number of characters of a list element.**
# 
# > Write a set of Python commands that determine the number of characters of the second element of a list. In case the element consists of more than 4 characters print 'True' otherwise print 'False'. Test your statements using the following lists `['angel', 'nightmare', 'poltergeist']` and `['darkness', 'king', 'fairy', 'owl']`.

# In[ ]:





# **2. Write a set of (or single) Python command(s) that compares the elements of a list.**
# 
# > Write a set of Python commands that compares the first and last elements of a list. In case both elements consist of the same characters print 'True' otherwise print 'False'. Test your statements using the following list `['BROOMSTICK', 'ghostly', 'mYstEriOUs', 'BROOMSTICK']` and `['darkness', 'king', 'fairy', 'owl']`.

# In[ ]:





# **3. Write a set of (or single) Python command(s) that removes elements of a list.**
# 
# > Write a set of Python commands to print a specified list after removing the 0th, 2th, 3th, and 5th element. Test your statements using the following list `['BROOMSTICK', 'Happy', 'mYstEriOUs', 'BROOMSTICK', 'Halloween', 'Poltergeist']`.

# In[ ]:





# ### 4. Fundamental Programming Structures

# As part of this lab, we want to have a closer look at three basic programming structures of Python:
# 
# > * **For-Loops** - used to iterate over a sequence of program satements.
# > * **Decision Structures** - used to anticipate conditions occurring while execution of a program.
# > * **Functions** - used to define a block of code which only runs when it is called.

# #### 4.1 Python Loop Structures

# To keep a program doing some useful work we need some kind of repetition, looping back over the same block of code again and again. Below we will describe the different kinds of loops available in Python.

# #### 4.1.1. The "For"-Loop and Lists

# The for loop that is used to iterate over elements of a sequence, it is often used when you have a piece of code which you want to repeat a specifc "n" number of time. The nature of a for-loop in Python is very straightforward  **"for all elements in a list, do this".**
# 
# Let's say that you have a list; you can then loop over the list elements using the `for` keyword like this:

# In[86]:


# list initialization
halloween_elements = ['cat', 'night', 'pumpkin', 100, 999]

# loop initialization and run
for anyname in halloween_elements: 
    print(anyname)


# **Note:** Python relies on the concept of indentation, using whitespace (or tabs), to define the scope in the code. Other programming languages such as Java or C# often use brackets or curly-brackets for this purpose.

# Let's have a look at another example of a for-loop:

# In[87]:


# init a list of numbers
numbers = [1, 10, 20, 30, 40, 50]

# init the result
result = 0

# loop initialization and run
for number in numbers:
    result = result + number
    # result += number

# print the result
print(result)


# To loop over a list of numbers, we can use Python's `range` function. The `range(lower_bound, upper_bound, step_size)` function generates a sequence of numbers, starting from the `lower_bound` to the `upper_bound`. The `lower_bound` and `step_size` parameters are optional. By default the lower bound is set to zero, the incremental step is set to one.

# In[88]:


# loop over range elements
for i in range(1, 10):
    
    # print current value of i
    print(i)


# To break out from a loop, you can use the keyword `break`. Let's have a look at the following example: 

# In[89]:


# loop over range elements
for i in range(1, 10000000000):
    
    # case: current value of i equals 3?
    if i == 3:
        
        # break: stop the loop
        break 
        
    # print current value of i
    print(i)


# In contrast, the `continue` keyword is used to tell Python to skip the rest of the statements in the current loop block and to continue to the next iteration of the loop.

# In[90]:


# loop over range elements
for i in range(1, 10):
    
    # case: current value of i equals 3?
    if i == 3:
        
        # continue: jump to next loop iteration 
        continue
    
    # print current value if i
    print(i)


# If you want access to the index of each element within the body of a loop, use the built-in enumerate function:

# In[91]:


halloween_elements = ['cat', 'night', 'pumpkin']
for idx, element in enumerate(halloween_elements):
    print('#%d: %s' % (idx + 1, element))


# When programming frequently, we want to transform one type of data into another. As a simple example, consider the following code that computes square numbers:

# In[92]:


nums = [0, 1, 2, 3, 4]
squares = []
for x in nums:
    squares.append(x ** 2)
print(squares)


# You can make this code simpler using a list comprehension:

# In[93]:


nums = [0, 1, 2, 3, 4]
squares = [x ** 2 for x in nums]
print(squares)


# List comprehensions can also contain conditions:

# In[94]:


nums = [0, 1, 2, 3, 4]
even_squares = [x ** 2 for x in nums if x % 2 == 0]
print(even_squares)


# #### 4.1.2. The "For"-Loop and Dictionaries

# Similarly, it is easy to iterate over the keys in a dictionary:

# In[95]:


d = {'pumpkin': 0, 'cat': 4, 'spider': 8}
for animal in d:
    legs = d[animal]
    print('A %s has %d legs' % (animal, legs))


# If you want access to keys and their corresponding values, use the items method:

# In[96]:


d = {'pumpkin': 2, 'cat': 4, 'spider': 8}
for animal, legs in d.items():
    print('A %s has %d legs' % (animal, legs))


# ### Exercises:

# We recommend you to try the following exercises as part of the lab:
# 
# **1. Write a Python loop that multiplies all elements of a list with 10.**
# 
# > Write a Python loop that multiplies all elements of a list with `66`. The input list is given by `range(0, 10)` and its output should result in a list as denoted by: `[0, 66, 132, 198, 264, 330, 396, 462, 528, 594]`.

# In[99]:





# **2. Write a Python loop that prints the numbers 1 to 10 backwards.**
# 
# > Write a Python loop that prints the numbers 0 to 10 backwards. The output of the loop should print the following: `10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0`.

# In[ ]:





# #### 4.2 Python Decision Structures

# Decision structures evaluate multiple expressions which produce **True** or **False** as an outcome. When solving a data science task, you often need to determine which action to take and which statements to execute if an outcome is **True** or **False** otherwise. 
# 
# Let's briefly recap Python's use of logical or mathematical conditions:

# In[73]:


# init sample variables
a = 4
b = 7


# In[74]:


print(a == b)  # equals
print(a != b)  # not equals
print(a < b)   # less than
print(a <= b)  # less than or equal to 
print(a > b)   # greater than
print(a >= b)  # greater than or equal to


# The mathematical conditions outlined above can be used in several ways, most commonly in if-statements. An if-statement is written by using the `if` keyword. Let's have a look at an example:

# In[75]:


# init sample variables
a = 4
b = 7

# test condition
if b > a:
    print("b is greater than a")


# In the example above we used two variables, `a` and `b`, which are used as part of the if-statement to test whether `b` is greater than `a`. As a is 4, and b is 7, we know that 7 is greater than 4, and so we print that "b is greater than a".

# We can easily enhance the if-statement above by additional condidtions by the `elif` keyword. The `elif` keyword is pythons way of saying "if the previous conditions were not true, then try this condition":

# In[76]:


a = 4
b = 4

# test condition 1
if b > a:
  print("b is greater than a")

# test condition 2
elif a == b:
  print("a and b are equal")

elif a != b:
    print("test check and so on... ")


# Finally, we can use the `else` keyword to catch any case which isn't found by the preceding conditions:

# In[77]:


a = 8
b = 4

# test condition 1
if b > a:
  print("b is greater than a")

# test condition 2
elif a == b:
  print("a and b are equal")

# all other cases
else:
  print("a is greater than b")


# In the example above the value assigned to a variable `a` is greater than the value assigned to `b`, so the first `if` condition is not true. Also the `elif` condition is not true, so we ultimatively go to the `else` condition and print that "a is greater than b".

# ### Exercises:

# We recommend you to try the following exercises as part of the lab:
# 
# **1. Write a Python decision structure that prints all the numbers from 0 to 6 except 4 and 7.**
# 
# > Write a Python decision structure that prints a number if it doesn't equal to 4 and 7. If the number equals 4 or 7 it should print 'forbidden number'.

# In[ ]:





# **2. Write a Python decision structure that evaluates if a number is a multiple of 5 and 7.**
# 
# > Write a Python decision structure that evaluates if number is a multiple of 5 and 7. Hint: You may want to use Python's percentage `%` operator as part of your case evaluation.

# In[ ]:





# Dictionary comprehensions: These are similar to list comprehensions, but allow you to easily construct dictionaries. For example:

# In[78]:


nums = [0, 1, 2, 3, 4]
even_num_to_square = {x: x ** 2 for x in nums if x % 2 == 0}
print(even_num_to_square)


# #### 4.3 Python Functions 

# A function is a block of organized, reusable code that is used to perform a single, related action. Functions provide better modularity for your application and allow for a high degree of reusable code. As you already saw, Python provides you with many built-in functions such as `print()`, etc. but you can also create your functions. These functions are called **user-defined functions**.
# 
# A function is a block of code which only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result. Python functions are defined using the `def` keyword.

# <img align="mid" style="width: 400px; height: auto" src="python-function.svg">

# (Source: https://swcarpentry.github.io/python-novice-inflammation/06-func/index.html.) 
# 
# Let's define our first function that takes a string as input parameter and prints it:

# In[79]:


# defines a printme function
def print_me(characters):
    
   # this prints a passed string into this function
   print(characters)


# Now, we can call our newly defined function using the function name followed by the arguments that we aim to pass in parenthesis:

# In[80]:


print_me(characters="I'm first call to user defined function!")
print_me(characters="Again second call to the same function")


# Isn't that fantastic? 

# Now that we understood the syntax to create customized functions, we can create even more complex functions. Let's implement a function that determines if a given integer number is positive, negative or zero using a decision structure and prints the result accordingly:

# In[81]:


# defines a sign evaluation function
def sign(x):
    
    # case: positive value
    if x > 0:
        
        # return the string 'positive'
        return 'positive'
    
    # case: negative value
    elif x < 0:
        
        # return the string 'negative'
        return 'negative'
    
    # else: other value
    else:
        
        # return the string 'zero'
        return 'zero'


# Now we call our function and print the result of sign evaluation for distinct values:

# In[82]:


print(sign(x=-1))
print(sign(x=0))
print(sign(x=1))


# We will often define functions to take optional keyword arguments. An optional argument is an argument that assumes a default value if a value is not provided in the function call for that argument. The following example provides an idea on default arguments, it prints the characters given in upper case if not specified different, like this:

# In[83]:


def hello(characters, loud=1633):
    
    # case: default - loud print enabled
    if loud:
        print('HELLO, %s' % characters.upper())
        
    # case: non-loud print enabled
    else:
        print('Hello, %s!' % characters)


# In[84]:


hello(characters='Helloween', loud=1000)


# In[85]:


hello(characters='Helloween', loud=False)


# ### Exercises:

# We recommend you to try the following exercises as part of the lab:
# 
# **1. Write a Python function to calculate the length of a string.**
# 
# >Write a Python function named **"string_length"** to calculate the length of an arbitrary string. The function should take an arbitrary string as an input and count the number of its characters. Test your function accordingly using various string values and print the results, e.g., input: 'Halloween', expected result: 9.

# In[ ]:





# **2. Write a Python program to get the largest number from a list.**
# 
# >Write a Python function named **"max_num_in_list"** to get the largest number from a list. The function should take an arbitrary list of integer values as an input and should return the integer that corresponds to the highest value. Test your function accordingly using various string values and print the results, e.g., input: [1, 5, 8, 3], expected result: 8.

# In[ ]:





# **3. Write a Python program to count the number of characters (character frequency) in a string.**
# 
# >Write a Python function named **"char_frequency"** to count the number of distinct characters occuring in it. The function should take an arbitrary string as an input and should return the count of occurance each individual character. Test your function accordingly using various string values and print the results, e.g., input: 'Happy Halllllloweeeeeen!', expected result: {'a': 2, ' ': 1, 'e': 6, 'H': 2, 'l': 6, 'o': 1, 'n': 1, 'p': 2, '!': 1, 'w': 1, 'y': 1}.

# In[ ]:





# **Bonus: Write a Python function that takes a list of words and returns the one exhibiting the most characters.**
# 
# >Write a Python function named **find_longest_word** that takes a list of words and returns the length of the longest word in the list. The function should take an arbitrary list of string values (words) as an input and should return the word that exhibits the most characters. Test your function accordingly using various lists of string values and print the results, e.g., input: ['Happy', 'Halloween', '2018'], expected result: 'Halloween'.

# In[ ]:





# ### [BONUS] 5. Basic Python Image Manipulations

# The Python Imaging Library (abbreviated as PIL, in newer versions known as Pillow), is a free library for the Python programming language that adds support for opening, manipulating, and saving many different image file formats. Using the PIL library in combination with the Numpy library allows for a great deal image analysis and manipulation:
# 
# Pls. note, that prior to using PIL you need to install the Python Image package. A brief installation instruction can be obtained from: https://pillow.readthedocs.io/en/5.3.x/installation.html.

# Upon successfully installation we can now import the PIL package:

# In[100]:


# use this statement to show plots inside your notebook
get_ipython().run_line_magic('matplotlib', 'inline')

# import the pil and the matplotlib libraries
from PIL import Image 
import numpy as np
import matplotlib.pyplot as plt


# PIL supports a wide variety of image file formats. To read files from disk, use the open() function in the Image module. You don’t have to know the file format to open a file. The library automatically determines the format based on the contents of the file. Let's open and plot the 'halloween.jpg' image file:

# #### 5.1. Image Loading and Plotting

# In[140]:


image = np.asarray(Image.open("halloween.jpg"))
plt.imshow(image, vmin=0, vmax=255)


# Let's have a look at the exact shape of the image:

# In[116]:


h, w, c = image.shape

print(h)   # prints the image height
print(w)   # prints the image width
print(c)   # prints the number of image color channels = 3 for red, green, blue (rgb)


# #### 5.2. Image Cropping

# Use PIL to extract the upper pumpkin of the image:

# In[141]:


upper_pumpkin = image[20:250, 20:300, :]
plt.imshow(upper_pumpkin, vmin=0, vmax=255)


# In[125]:


upper_pumpkin.shape


# Let's extract the distinct (RGB) color channels of the image:

# In[142]:


# extraction of the red color channel
red_channel = np.zeros(upper_pumpkin.shape, dtype='uint8')
red_channel[:,:,0] = upper_pumpkin[:,:,0]

plt.imshow(red_channel)


# In[143]:


# extraction of the green color channel
green_channel = np.zeros(upper_pumpkin.shape, dtype='uint8')
green_channel[:,:,1] = upper_pumpkin[:,:,1]

plt.imshow(green_channel)


# In[144]:


# extraction of a blue color channel
blue_channel = np.zeros(upper_pumpkin.shape, dtype='uint8')
blue_channel[:,:,2] = upper_pumpkin[:,:,2]

plt.imshow(blue_channel)


# #### 5.3. Image Manipulation

# Greyscale the image by setting the third image channel to mean of all color values:

# In[106]:


gray = upper_pumpkin.mean(axis=2)
plot = plt.imshow(gray, cmap=plt.cm.gray, vmin=0, vmax=255)


# To learn more about PIL and its capabilites visit: https://pillow.readthedocs.io.

# ### Lab Summary:

# In this second lab, the basic data types and containers of the Python programming language are presented. The code and exercises presented in this lab may serve as a starting point for more complex and tailored analytics. 

# You may want to execute the content of your lab outside of the Jupyter notebook environment, e.g. on a compute node or a server. The cell below converts the lab notebook into a standalone and executable python script. Pls. note, that to convert the notebook you need to install the Python **nbconvert** package available via https://pypi.org/project/nbconvert/5.3.1/ before running the command below.

# In[5]:


get_ipython().system('jupyter nbconvert --to script mldl_lab_02.ipynb')


# In[ ]:




