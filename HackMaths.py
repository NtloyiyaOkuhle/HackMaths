import math
import sympy
import pint

# Create an empty dictionary to store previously solved problems
prev_problems = {}

# Create a dictionary to store the variables and their values
variables = {}

# Create a UnitRegistry object from pint
ureg = pint.UnitRegistry()

# Define the available functions
functions = {
    'sin': sympy.sin,
    'cos': sympy.cos,
    'tan': sympy.tan,
    'log': sympy.log,
    'exp': sympy.exp,
    'sqrt': sympy.sqrt,
    'abs': sympy.Abs,
    'factorial': sympy.factorial,
    'integrate': sympy.integrate,
    'diff': sympy.diff,
    'solve': sympy.solve,
    'simplify': sympy.simplify,
    'expand': sympy.expand,
    'factor': sympy.factor,
    'cancel': sympy.cancel,
}

# Define a function to evaluate a mathematical expression
def evaluate(expression):
    # Replace variables with their values
    for var, val in variables.items():
        expression = expression.replace(var, str(val))

    # Parse the expression with sympy
    expr = sympy.sympify(expression)

    # Evaluate the expression with units conversion
    try:
        # Try to evaluate the argument as a number with units
        arg = ureg(arg_str)
        if arg.dimensionality == pint.dimensionless.dimensionality:
            # The argument is a pure number, without units
            arg = float(arg)
        else:
            # The argument has units, convert to base units
            arg = arg.to_base_units().magnitude
    except pint.UndefinedUnitError:
        # If the argument is not a number with units or a variable, raise an error
        raise ValueError(f'Invalid argument: {arg_str}')


    return result, unit

# Define a function to format a number with a specified number of decimal places
def format_number(number, decimals):
    if decimals is None:
        return str(number)
    else:
        return f'{number:.{decimals}f}'

# Define a function to display the list of available functions
def display_functions():
    print('Available functions:')
    for func in sorted(functions.keys()):
        print(f'- {func}(...)')

# Define a function to display the history of solved problems
def display_history():
    print('History of solved problems:')
    for problem, result in prev_problems.items():
        print(f'{problem} = {format_number(result[0], result[1])}')

# Define a function to display the options menu
def display_options():
    print('Options:')
    print('- Set the number of decimal places to display (e.g., decimals=2)')
    print('- Display the list of available functions (type "functions")')
    print('- Display the history of solved problems (type "history")')
    print('- Exit the program (type "exit")')

while True:
    # Get user input
    user_input = input('Enter a mathematical problem to solve (or "exit" to quit): ')

    # Check if the user wants to exit
    if user_input.lower() == 'exit':
        break

    # Check if the user wants to display the list of available functions
    if user_input.lower() == 'functions':
        display_functions()
        continue

    # Check if the user wants to display the history of solved problems
    if user_input.lower() == 'history':
        display_history()
        continue
        
    # Check if the user wants to set the number of decimal places to display
    if 'decimals=' in user_input:
        try:
            decimals = int(user_input.split('=')[1])
        except ValueError:
            raise ValueError('Invalid input: decimals must be an integer')
        continue
    else:
        decimals = None


    # Check if the problem has already been solved
    if user_input in prev_problems:
        result, unit = prev_problems[user_input]
        print(f'Result (from history): {format_number(result, decimals)} {unit}')
        continue

    # Split the problem into function and argument(s)
    if '(' not in user_input:
        raise ValueError('Invalid input: missing parentheses')
    parts = user_input.split('(')
    function_name = parts[0]
    args_str = parts[1].strip(')')


    # Parse the arguments
    args = []
    for arg_str in args_str.split(','):
        arg_str = arg_str.strip()
        # Check if the argument is a variable
        if arg_str in variables:
            arg = variables[arg_str]
        else:
            try:
                # Try to evaluate the argument as a number with units
                arg = ureg(arg_str).to_base_units().magnitude
            except pint.UndefinedUnitError:
                # If the argument is not a number with units or a variable, raise an error
                raise ValueError(f'Invalid argument: {arg_str}')
        args.append(arg)

    # Call the function with the parsed arguments
    if function_name not in functions:
        raise ValueError(f'Invalid function name: {function_name}')
    function = functions[function_name]
    result, unit = function(*args)

    # Store the result in the history dictionary
    prev_problems[user_input] = (result, unit)
    # Display the result
    print(f'Result: {format_number(result, decimals)} {unit}')
