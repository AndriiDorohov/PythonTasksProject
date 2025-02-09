# Chapter 6, 7, 8, 10 (Python functions)

# Task 1: String Manipulation Function
# Problem:
# 1. Write a function format_name(name, title="Mr./Ms.") that
# takes two parameters:
# name: a string representing a person's name.
# title: a string with a default value of "Mr./Ms.".
# 2. The function should return a formatted string like:
# "Title: [title], Name: [name]".
# 3. The function should handle cases where name is a single
# name (like "Alice") or a full name (like "Alice Johnson").
# If the name consists of more than one word, only the first word
# should be considered as the first name.
# Example Output:

# Title: Mr., Name: Alice
# Title: Dr., Name: John

def format_name(name, title="Mr./Ms."):
    return  (f'Title: {title}, Name: {name}')

name: str
title: str
key = False

while not key:
    name = input("Input Name:").capitalize().strip()
    if " " in name:
        name = name.split(" ")
        name = name[0]

    if name.isalpha():
        key = True
    else:
        print("Wrong name")

title = input("Input title:").capitalize()
if not title.endswith('.'):
    title += "."
result = format_name(name, title)
print(result)
