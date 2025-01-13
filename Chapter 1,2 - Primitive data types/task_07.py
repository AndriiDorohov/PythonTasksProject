# Task 7: Using is Operator with Primitive Types
# Problem:
# 1. Create two integer variables x = 500 and y = 500.
# 2. Use the is operator to check if x and y refer to the same
# object in memory and print the result.
# 3. Create two variables p = 10 and q = 10.
#  - Use the is operator to check if p and q refer to the same
#  object in memory and print the result.

x = 500
y = 500
p = 10
q = 10
print("\nTASK 7")
# I get True in both cases, so I additionally printed the identifier values,
# which in my environment also match, possibly due to optimization or other factors.
print(id(x), id(y))
print(id(p), id(q))
print(x is y)
print(p is q)