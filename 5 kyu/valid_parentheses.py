"""
Description:
Write a function called that takes a string of parentheses, and determines if the order of the parentheses
is valid. The function should return true if the string is valid, and false if it's invalid.

Examples
"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true
Constraints
0 <= input.length <= 100

Along with opening (() and closing ()) parenthesis, input may contain any valid ASCII characters.
Furthermore, the input string may be empty and/or not contain any parentheses at all.
Do not treat other forms of brackets as parentheses (e.g. [], {}, <>).
"""


def valid_parentheses(string):
    """
    Checks if the order of the parentheses is valid.
    :param string: string
    :return: bool
    """
    parentheses = {'(': ')'}

    check_list = []

    for char in string:
        if char.isalpha():
            continue
        elif char in parentheses:
            check_list.append(parentheses[char])
        elif not check_list or char != check_list.pop():
            return False
    return not check_list


print(valid_parentheses("zo(ruhlhr(du)stshn((jbw(am)az)d(tqxvmvhnbl)"))
