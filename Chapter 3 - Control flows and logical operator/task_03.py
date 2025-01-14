# Task 3: Logical Operator Practice
# Problem: Given three boolean variables, a = True, b = False, c = True, write a program that:
# 1. Evaluates and prints the result of the following conditions:
# a and b
# a or b
# not b
# (a and c) or b
# a and (b or c)
# 2. Explain in a comment why each result is True or False.

print("\nTASK 3")
a = True
b = False
c = True
print("a and b = ", a and b)
# якщо a = True то переходимо до значенн b, якщо a = False,
# то отримуємо False
print("a or b = ", a or b)
# якщо a = True то повертаємо True інакше дивимось b і повертаємо
# його значення
print("not b = ", not b)
# повертає True, якщо вираз дорівнює False і навпаки, інвертує значення
print("(a and c) or b = ", (a and c) or b)
# and повератє True, бо a і c дорівнюють True. or поверне True, якщо хоча б
# одне значення дорівнює True
print("a and (b or c) = ", a and (b or c))
# or між b і c повертає True, якщо хоча б одне значення є True. And поверне
# True, тому що обидва значення True