"""You've been collecting change all day, and it's starting to pile up in your pocket,
but you're too lazy to see how much you've found.

Good thing you can code!

Create change_count() to return a dollar amount of how much change you have!

Valid types of change include:

penny: 0.01
nickel: 0.05
dime: 0.10
quarter: 0.25
dollar: 1.00
These amounts are already preloaded as floats into the CHANGE dictionary for you to use!

You should return the total in the format $x.xx.

Examples:

change_count('nickel penny dime dollar') == '$1.16'
change_count('dollar dollar quarter dime dime') == '$2.45'
change_count('penny') == '$0.01
change_count('dime') == '$0.10'
Warning, some change may amount to over $10.00!"""
from decimal import *


def change_count(change):
    getcontext().prec = 2
    change_value = 0.00
    for coin in change.split():
        change_value += CHANGE[coin]
    change_total = Decimal(change_value)
    return '$' + str(format(change_total, '2.2f'))


def change_count2(change):
    total = sum(CHANGE[coin] for coin in change.split())
    return '$' + str(format(total, '2.2f'))


CHANGE = {'penny': 0.01,
          'nickel': 0.05,
          'dime': 0.10,
          'quarter': 0.25,
          'dollar': 1.00
          }


print(change_count('dollar dollar dollar dollar dollar dollar dollar dollar dollar dollar penny'))
print(change_count2('dollar dollar dollar dollar dollar dollar dollar dollar dollar dollar penny'))