<b>Prompt Until</b>
===================


##What is it?
Prompt Until is a tiny python library that does exactly what it name says. It is basically input(), but it takes a lambda to tell if the entered value is valid. If the entered value is valid it will return it, otherwise, it will ask the user to enter another input.

------------------------

##Some use cases w/ Examples

###Asking a user for an integer
If the user is prompted for an integer, there is an easy way to make sure that they enter an integer, and parse it in the process.
####Before
```python
# this is bad. We will crash if user entered something not
# an integer.
integer = int(input("Enter an int: "))
```
####After
```python
import prompter

# prompt the user until they enter an integer
integer = prompter.prompt_until(
    "Enter an int: ",  # passed to input()
    prompter.is_int,  # the (lambda) function that evaluates the entered info
    fail_msg="You didn't enter an integer! Please try again",  # printed when not an int
    success_action=int)  # function to run on success

# because int returns an int version of the string
# (something other than None), prompt_until will return the result of int(input),
# so there is no need to surround call with int()

# Shows that input was casted to int. "1" + 100 = "1100", 1 + 100 = 101
print(integer + 100)
```

####Now, lets say you want to add a min/max value for the entered integer.
```python
# just change the is_valid argument (2nd parameter) to 
lambda ins: is_int(ins) and MINVALUE < int(ins) < MAXVALUE
```
