"""Check to see if a string has the same amount of 'x's and 'o's.
The method must return a boolean and be case insensitive.
The string can contain any char.

Examples input/output:

XO("ooxx") => True
XO("xooxx") => False
XO("ooxXm") => True
XO("zpzpzpp") => True // when no 'x' and 'o' is present should return true
XO("zzoo") => False"""


def xo(s):
    x = s.lower().count('x')
    o = s.lower().count('o')
    if x == o:
        return True
    else:
        return False


if __name__ == "__main__":
    text = "oaxgoxhxooxweooxXm"
    print(xo(text))
