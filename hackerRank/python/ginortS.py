# You are given a string .
#  contains alphanumeric characters only.
#  Your task is to sort the string  in the following manner:

# All sorted lowercase letters are ahead of uppercase letters.
# All sorted uppercase letters are ahead of digits.
# All sorted odd digits are ahead of sorted even digits.
# Input Format

# A single line of input contains the string .

# Constraints

# Output Format

# Output the sorted string .

# Sample Input

# Sorting1234
# Sample Output

# ginortS1324

# Enter your code here. Read input from STDIN. Print output to STDOUT
s = input()
print(*sorted(s, key=lambda x: (x.isdigit(), x.isdigit() and int(x) % 2 == 0, x.isupper(), x.islower(), x)), sep='')