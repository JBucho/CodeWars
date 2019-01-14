"""The following code was thought to be working properly,
however when the code tries to access the age of the person instance it fails.

person = Person('Yukihiro', 'Matsumoto', 47)
print(person.full_name)
print(person.age)"""


class Person:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        # full_name = [first_name, last_name]  # full_name = f"{first_name} {last_name}" !(only python 3.6+)
        self.full_name = '{} {}'.format(first_name, last_name)


matz = Person('Yukihiro', 'Matsumoto', 47)
print(matz.full_name)
print(matz.age)

joe = Person('Joe', 'Smith', 30)
print(joe.full_name)
print(joe.age)