"""oday, we're discussing data types. Check out the Tutorial tab for learning materials and an instructional video!

Task
Complete the code in the editor below. The variables i, d, and  s are already declared and initialized for you. You must:

Declare 3 variables: one of type int, one of type double, and one of type String.
 Read 3 lines of input from stdin (according to the sequence given in the Input Format section below) and initialize your  variables.
Use the  + operator to perform the following operations:
Print the sum of i  plus your int variable on a new line.
Print the sum of d  plus your double variable to a scale of one decimal place on a new line.
Concatenate s with the string you read as input and print the result on a new line.
Note: If you are using a language that doesn't support using + for string concatenation (e.g.: C), you can just print one variable immediately following the other on the same line. The string provided in your editor must be printed first,
 immediately followed by the string you read as input."""


i = 4
d = 4.0
s = 'HackerRank '
# Declare second integer, double, and String variables.

# Read and save an integer, double, and String to your variables.
a=int(input())
b=float(input())
c=input()


# Print the sum of both integer variables on a new line.
sum1=i+a
print(int(sum1))
# Print the sum of the double variables on a new line.
sum2=d+b
print(float(sum2))

# Concatenate and print the String variables on a new line
print(f"HackerRank {c}")
