# Bonus Task 9: Create a Custom Iterator for a Fibonacci Sequence
# Problem:
# Create a custom iterator class called FibonacciIterator
# that generates numbers in the Fibonacci sequence. The
# iterator should take an input n, which specifies the maximum
# number of Fibonacci numbers to generate.
# Implement the __iter__ and __next__ methods to make the class
# an iterator.
# Use the iterator to generate and print the Fibonacci sequence
# up to n terms.
# Example Input:
# fib = FibonacciIterator(5)
# for num in fib:
#     print(num)

# Expected Output:
# 0
# 1
# 1
# 2
# 3

# Challenge:
# Extend the iterator to raise a StopIteration exception when
# the maximum n is reached.
# Use the iterator with the list() function, e.g.,
# list(FibonacciIterator(7)) should output [0, 1, 1, 2, 3, 5, 8].


# These tasks cover a range of OOP principles from basic
# classes and objects to advanced techniques like method
# overriding, dunder methods, inheritance, and class/static methods.


class FibonacciIterator:
    def __init__(self, n: int) -> None:
        self.n = n
        self.a1 = 0
        self.a2 = 1
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count == 0:
            self.count += 1
            return self.a1
        elif self.count == 1:
            self.count += 1
            return self.a2
        elif self.count < self.n:
            result = self.a1 + self.a2
            self.a1 = self.a2
            self.a2 = result
            self.count += 1
            return result
        else:
            raise StopIteration


fib = FibonacciIterator(7)
for num in fib:
    print(num)

print(list(FibonacciIterator(7)))
