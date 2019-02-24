"""A pangram is a sentence that contains every single letter of the alphabet at least once.
For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram,
because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not.
Ignore numbers and punctuation.
"""

import string


def is_pangram(s):
    """
    Checks if given string is a pangram.
    :param s: string
    :return: boolean => True if given string is a pangram, False if it is not a pangram.
    """
    return True if all(letter in s.lower() for letter in string.ascii_lowercase) else False


def is_pangram2(s):
    """
    Checks if given string is a pangram.
    :param s: string
    :return: boolean => True if given string is a pangram, False if it is not a pangram.
    """
    return set(string.ascii_lowercase) <= set(s.lower())


if __name__ == "__main__":

    pangram = "Pack my box with five dozen liquor jugs."
    pangram2 = "The quick brown fo. jumps, over the lazy dog!"
    pangram3 = "The quick brown fox jumps over the lazy dog"

    print(is_pangram(pangram))
    print(is_pangram2(pangram))
    print()
    print(is_pangram(pangram2))
    print(is_pangram2(pangram2))
    print()
    print(is_pangram(pangram3))
    print(is_pangram2(pangram3))
