"""
The MIT License (MIT)

Copyright (c) 2015 Will Bresnahan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

A program that prompts the user for input until a condition is reached.
It is not completely useless.
"""
__author__ = "Will (n9Mtq4) Bresnahan"


def prompt_until(prompt, is_valid, fail_msg=None, fail_action=None, success_msg=None, success_action=None):
    """
    Will prompt the user with the prompt, until is_valid returns true.
    If is_valid is false, it will print fail_msg, and/or run fail_action.
    If fail_action returns something, other than None, it will return the result of fail_action.
    If is_valid is true, it will print success_msg, and/or run success_action.
    If success_action returns something, other than None, it will return the result of success_action.
    :param prompt: The string to prompt the user with
    :param is_valid: The lambda to decide if the input is valid
    :param fail_msg: The message to print if the input isn't valid
    :param fail_action: The action to do if the input isn't valid
    :param success_msg: The message to print if the input is valid
    :param success_action: The action to do if the input is valid
    :return: The valid input
    """
    while True:
        # much code. very logic. many dense. (http://goo.gl/azriO7)
        user_entered = input(prompt)  # ask the user for input
        if is_valid(user_entered):  # if the lambda(input) returned true
            if success_msg is not None:  # try to print success messafe
                print(success_msg)
            if success_action is not None:  # try to run the success action
                re = success_action(user_entered)
                if re is not None:  # if success_action returned something, bubble it
                    return re
            return user_entered  # it succeeded, so return the user input
        else:  # if the input isn't valid
            if fail_msg is not None:
                print(fail_msg)
            if fail_action is not None:  # try to run the fail action
                re = fail_action(user_entered)
                if re is not None:  # if fail_action returned something, bubble it
                    return re


def is_in_list(object, list):
    """
    Checks if object is in the list.
    :param object: The object to look for
    :param list: The list to look for the object in
    :return: A boolean if the object is in the list
    """
    for o in list:
        if o == object:
            return True
    return False


def is_in_dictionary(keyname, dictionary):
    """
    Checks if the keyname is in the dictionary.
    :param keyname: The keyname to look for
    :param dictionary: The dictionary to look for it in
    :return: A boolean if the object is in the list
    """
    for key in dictionary:
        if key == keyname:
            return True
    return False


def is_bool(boolean):
    """
    Checks if the string can be parsed to a boolean
    :param boolean: The boolean in STRING form
    :return:
    """
    try:
        parse_bool(boolean)
        return True
    except ValueError:
        return False


def parse_bool(boolean):
    """
    Turns a string into a boolean.
    true, yes, y, or t -> True
    false, no, n, or f -> False
    anything else raises a ValueError
    :param boolean: The boolean in STRING format
    :return: A boolean
    """
    b = boolean.lower()
    if b == "true" or b == "yes" or b == "y" or b == "t":
        return True
    elif b == "false" or b == "no" or b == "n" or b == "f":
        return False
    else:
        raise ValueError("Invalid Boolean %s" % boolean)


def ran_without_errors(funct, *args):
    """
    Runs the function with the args.
    Returns true if it ran without errors,
    false if it didn't have any errors
    :param funct: The function to run.
    :param args: The args to pass into the function
    :return: A boolean - true if the function ran without errors, false if it didn't
    """
    try:
        funct(args)
        return True
    except Exception:
        return False


def is_int(str):
    """
    Checks if the string is an integer
    :param str: The string
    :return: A boolean if the str can be int()
    """
    try:
        int(str)
        return True
    except ValueError:
        return False


def is_float(str):
    """
    Checks if the string is a float
    :param str: The string
    :return: A boolean if the str can be float()
    """
    try:
        float(str)
        return True
    except ValueError:
        return False
