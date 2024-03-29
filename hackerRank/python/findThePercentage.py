# The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. 
# Print the average of the marks array for the student name provided, showing 2 places after the decimal.

if __name__ == '__main__':
    n = int(input("Enter number of students: "))
    student_marks = {}
    for _ in range(n):
        name, *line = input("Enter student name and marks: ").split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input("Enter a name: ")
    query_scores = student_marks[query_name]
    print("{0:.2f}".format(sum(query_scores) / len(query_scores)))

# Sample Input
# 3
# Manu 67 68 69
# Kanu 70 98 63
# Hani 52 56 60
# Hani

# Sample Output
# 56.00