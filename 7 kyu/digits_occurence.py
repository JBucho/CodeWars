"""We need a method in the List Class that may count specific digits from a given list of integers.
This marked digits will be given in a second list. The method .count_spec_digits()/.countSpecDigits()
will accept two arguments, a list of an uncertain amount of integers integers_lists/integersLists
(and of an uncertain amount of digits, too) and a second list, digits_list/digitsList that has the
specific digits to count which length cannot be be longer than 10 (It's obvious, we've got ten digits).
The method will output a list of tuples, each tuple having two elements, the first one will be a digit
to count, and second one, its corresponding total frequency in all the integers of the first list.
This list of tuples should be ordered with the same order that the digits have in digitsList"""


class List(object):

    @staticmethod
    def count_spec_digits(i_list, d_list):
        s = ''.join(str(i) for i in i_list)
        return [(d, s.count(str(d))) for d in d_list]


if __name__ == '__main__':

    integers_list = [113, 21, 123, 3, 1, 22, 31, 42]
    digits_list = [1, 3, 2]

    L = List()
    print(L.count_spec_digits(integers_list, digits_list))
