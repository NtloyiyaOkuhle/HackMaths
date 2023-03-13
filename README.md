# HackMaths
 Python program that provides a simple command-line interface for solving mathematical problems using the SymPy library and units conversion using the Pint library.

Here is how you can use the code:

    Install the required libraries: SymPy and Pint. You can install them using pip by running the following commands in the terminal:

pip install sympy
pip install pint

Copy the code into a Python file (e.g., calculator.py).

Run the Python file in a terminal by navigating to the directory where the file is located and running the following command:

python calculator.py

Enter a mathematical problem to solve at the prompt. For example:

css

Enter a mathematical problem to solve (or "exit" to quit): sin(pi/2)

The program will solve the problem and display the result:

makefile

Result: 1.0

You can also use variables in your expressions. For example:

less

Enter a mathematical problem to solve (or "exit" to quit): a + 2*b

The program will prompt you to enter the values of the variables a and b. After entering the values, the program will solve the problem and display the result.

The program supports various functions, including sin, cos, tan, log, exp, sqrt, abs, factorial, integrate, diff, solve, simplify, expand, factor, and cancel. You can use these functions in your expressions. For example:

css

Enter a mathematical problem to solve (or "exit" to quit): integrate(x**2, x)

The program will solve the integral and display the result:

makefile

Result: x**3/3

The program also allows you to set the number of decimal places to display by typing decimals= followed by the number of decimal places. For example:

css

Enter a mathematical problem to solve (or "exit" to quit): sin(pi/2) decimals=2

The program will solve the problem and display the result with 2 decimal places:

makefile

Result: 1.00

The program keeps a history of previously solved problems, which you can access by typing history at the prompt. For example:

vbnet

Enter a mathematical problem to solve (or "exit" to quit): sin(pi/2)
Result: 1.0

Enter a mathematical problem to solve (or "exit" to quit): history
History of solved problems:
sin(pi/2) = 1.0
To exit the program, type exit at the prompt.
