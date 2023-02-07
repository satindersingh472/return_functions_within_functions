# define a function name calculate maths
#define add, sub , multiply and divide functions with in calculate maths functions



def calculate_maths(operation):
    def add(n1,n2):
        return n1 + n1
    def subtract(n1,n2):
        return n1 - n2
    def divide(n1,n2):
        return n1/n2
    def multiply(n1,n2):
        return n1 * n2


    if operation == '+':
        return add
    elif operation == '-':
        return subtract
    elif operation == '/':
        return divide
    elif operation == '*':
        return multiply

print('please enter the operation, +,-,/,*')
operation = calculate_maths(input())
print(operation(4,4))







