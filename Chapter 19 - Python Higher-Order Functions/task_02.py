# Task 2: Function Returning a Function
# Problem:
# Create a function make_adder(add_value) that returns
# a function adder:
# The returned adder function takes a number and adds
# the add_value provided to make_adder.
# Use make_adder to create an incrementer function that
# increments a number by 1. Test it on an input value.
# Example Output:

# 6


def make_adder(add_value):

    def adder(number):
        print(add_value + number)

    return adder


new = make_adder(5)
new(1)
