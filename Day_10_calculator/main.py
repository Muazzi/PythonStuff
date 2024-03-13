import  art
print(art.logo)
calculator = {}
#input
# number
first_num = int(input('whats the first number'))
print('+')
print('-')
print('*')
print('/')
# +
# -
# *
# /

operation = input('Pick an operation :')
# Whats the next number :?
second_num = int(input("What's the next number?:"))
# 5/2 = 2. 5
# Type 'y' to continue calculating with the above result(2.5) , or type 'n' to start a new calculation

def performOperation(num1 ,num2,operation):
    total=0
    match operation:
        case '+':
            total = num1 +num2
        case '-':
            total = num1 - num2
        case '*':
            total = num1 * num2
        case '/':
            total = num1/num2
    return  total

next_operation = input("# Type 'y' to continue calculating with the above result(2.5) , or type 'n' to start a new calculation").casefold()

next_operation =next_operation.casefold()
match next_operation :
    case 'n':
        first_num =0
        second_num = 0
