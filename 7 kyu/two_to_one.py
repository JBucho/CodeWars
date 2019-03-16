"""Take 2 strings s1 and s2 including only letters from ato z. Return a new sorted string,
the longest possible, containing distinct letters,

each taken only once - coming from s1 or s2. #Examples: ``` a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq" longest(a, b) -> "abcdefklmopqwxy"
a = "abcdefghijklmnopqrstuvwxyz" longest(a, a) -> "abcdefghijklmnopqrstuvwxyz" ``` """


import string


def longest(s1, s2):
    el = [i for i in string.ascii_lowercase if i in s1 or i in s2]

    return ''.join(el)


print(longest("aretheyhere", "yestheyarehere"))
print(longest("abcdefghijklmnopqrstuvwxyz", "xxxxyyyyabklmopq"))
