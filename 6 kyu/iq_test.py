""" Bob is preparing to pass IQ test. The most frequent task in this test is to find out which one of the given numbers
differs from the others. Bob observed that one number usually differs from the others in evenness. Help Bob — to check
his answers, he needs a program that among the given numbers finds one that is different in evenness, and return a
position of this number.

! Keep in mind that your task is to help Bob solve a real IQ test, which means
indexes of the elements start from 1 (not 0)

##Examples :

iq_test("2 4 7 8 10") => 3 // Third number is odd, while the rest of the numbers are even

iq_test("1 2 1 1") => 2 // Second number is even, while the rest of the numbers are odd """


def iq_test(numbers):
    numbers = numbers.split(' ')

    for i in range(0, len(numbers)):
        if int(numbers[i]) % 2 != int(numbers[i - 1]) % 2 and int(numbers[i]) % 2 != int(numbers[i - 2]) % 2:
            return i + 1
        else:
            i += 1
            continue


print(iq_test('16 10 22 10 4 6 10 4 34 50 48 34 44 50 4 26 26 42 48 10 48 46 18 42 20 28 18 34 16 48 40 44 31'))
