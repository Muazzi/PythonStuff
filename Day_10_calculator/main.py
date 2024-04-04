import  art
print(art.logo)
calulator_list = []
def pickOperation():
    print('+')
    print('-')
    print('*')
    print('/')
    operation = input('Pick an operation :')
    return  operation

def performOperation(num1 ,num2,operation):
    match operation:
        case '+':
            return num1 + num2
        case '-':
            return num1 - num2
        case '*':
            return  num1 * num2
        case '/':
            return   num1/num2


# read in one number at a time
# number->operation->number
# keep track of the total

in_operation = False

while not in_operation:
    first_num  = 0
    second_num = 0
    if len(calulator_list)==0:
        first_num = int(input('whats the first number: ? '))
        calulator_list.append(first_num)

    second_num = int(input("What's the next number?:"))
    calulator_list.append(second_num)
    operation = pickOperation()

    result = performOperation(num1=calulator_list[0], num2=calulator_list[1], operation=operation)
    print(
        f"{first_num}{operation}{second_num} = {performOperation(num1=first_num, num2=second_num, operation=operation)} ")

    next_operation = input(
        f"# Type 'y' to continue calculating with the above result({result}) , or type 'n' to start a new calculation").casefold()

    next_operation = next_operation.casefold()
    match next_operation:
        case 'n':
            calulator_list.clear()

        case 'y':
            operation = pickOperation()
            calulator_list[0] = result
            second_num = int(input("What's the next number?:"))
            calulator_list.append(second_num)
            result2 = performOperation(num1=result, num2=calulator_list[1], operation=operation)

            print(
                f"{result}{operation}{second_num}= {result2}")
            result = result2
        case _:
            in_operation = True
            break




#program












