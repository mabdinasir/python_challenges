# Question 9
# Level 2

'''
Question£º Write a program that accepts sequence of lines as input and 
prints the lines after making all characters in the sentence capitalized. 
Suppose the following input is supplied to the program: 
    # Hello world Practice makes perfect 
Then, the output should be: 
        # HELLO WORLD PRACTICE MAKES PERFECT

Hints: In case of input data being supplied to the question, 
it should be assumed to be a console input.
'''

# Solution:

lines = []
while True:
    inputString = input("Enter a line of words: ")
    if inputString:
        lines.append(inputString.upper())
    else:
        break

for sentence in lines:
    print(sentence, end="")  