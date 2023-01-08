#!/bin/python

#string1 = "hello, how are you?are you!ok"

string1 = input("enter words: ")

replacements = (' ', ',', '?', '!')

for regexp in replacements:
  string1 = string1.replace(regexp, ' ')

output_string = string1.split()

print("delimeted string: ", output_string)

longest_word = max(output_string, key = len)

print("the longest wotd in the string: ", longest_word)
