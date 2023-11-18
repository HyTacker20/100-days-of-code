def calculate(first_num: int | float, second_num: int | float, operation: str):
    return eval(f"{first_num} {operation} {second_num}")


def calculator(result=None):
    first_number = float(input("What's the first number?: ")) if not result else result
    print('+\n-\n*\n/')
    operation = input("Pick an operation: ")
    next_number = float(input("What's the next number?: "))
    result = calculate(first_number, next_number, operation)
    print(f'{first_number} {operation} {next_number} = {result}')
    to_continue = input(f"Type 'y' to continue calculating with {result}, "
                        f"or type 'n' to start a new calculation: ") == 'y'
    if to_continue:
        calculator(result)


if __name__ == '__main__':
    calculator()
