import sympy
from sympy import symbols, Eq, solve, Integral, Derivative, Matrix, lambdify
from sympy.plotting import plot

# Dictionary to store previously solved problems
prev_problems = {}

#Define function for solving problems
def solve_problem(problem_str):
    # Check if the problem is an equation
    if "=" in problem_str:
        # Parse the equation
        left, right = problem_str.split("=")
        expr = sympy.parsing.sympy_parser.parse_expr(left) - sympy.parsing.sympy_parser.parse_expr(right)

        # Solve the equation
        solutions = solve(expr, symbols('x'))

    # Check if the problem is a system of equations
    elif 'system' in problem_str:
        eqns = problem_str.split(',')
        eqns = [sympy.parsing.sympy_parser.parse_expr(eqn) for eqn in eqns]
        vars = []
        for eqn in eqns:
            vars += list(eqn.free_symbols)
        vars = sorted(set(vars), key=lambda var: str(var))
        solutions = sympy.solve(eqns, vars)

    # Check if the problem is a polynomial equation
    elif 'polynomial' in problem_str:
        expr = sympy.parsing.sympy_parser.parse_expr(problem_str.replace('polynomial', ''))
        solutions = sympy.roots(expr, multiple=True)

    else:
        # Parse the problem into a SymPy expression
        expr = sympy.parsing.sympy_parser.parse_expr(problem_str)

        # Check the type of the problem and solve accordingly
        if isinstance(expr, Eq):
            # Solve equation
            solutions = solve(expr, symbols('x'))
        elif isinstance(expr, Integral):
            # Solve integral
            solutions = sympy.integrate(expr, symbols('x'))
        elif isinstance(expr, Derivative):
            # Solve derivative
            solutions = sympy.diff(expr, symbols('x'))
        elif isinstance(expr, Matrix):
            # Solve matrix operations
            solutions = expr.doit()
        else:
            # Solve generic problem
            solutions = sympy.simplify(expr)

    # Check for additional functionality
    if 'sin' in problem_str or 'cos' in problem_str:
        solutions = sympy.solveset(expr, symbols('x'))
    elif 'tan' in problem_str:
        expr = sympy.parsing.sympy_parser.parse_expr(problem_str.replace('tan', 'sympy.tan'))
        solutions = expr.evalf()
    elif 'limit' in problem_str:
        expr, x, a = problem_str.split(',')
        expr = sympy.parsing.sympy_parser.parse_expr(expr)
        a = float(a)
        solutions = sympy.limit(expr, symbols(x), a)
    elif 'second derivative' in problem_str:
        expr = problem_str.replace('second derivative of ', '')
        expr = sympy.parsing.sympy_parser.parse_expr(expr)
        solutions = sympy.diff(expr, symbols('x'), 2)
    elif 'heat equation' in problem_str:
        u = sympy.Function('u')(symbols('x'), symbols('y'))
        eq = sympy.Eq(sympy.diff(u, symbols('x'), symbols('x')) + sympy.diff(u, symbols('y'), symbols('y')), 0)
        solutions = sympy.pde.pdsolve(eq)
    elif 'plot' in problem_str:
        # Parse the function and plot
        expr = sympy.parsing.sympy_parser.parse_expr(problem_str.replace('plot ', ''))
        p = plot(expr, show=False)
        p.show()
        return "Graph displayed."
    elif 'numeric' in problem_str:
        # Parse the function, convert to a lambda function, and evaluate numerically
        expr = sympy.parsing.sympy_parser.parse_expr(problem_str.replace('numeric ', ''))
        f = lambdify(x, expr)
        a, b = [float(x) for x in input("Enter the start and end points: ").split()]
        n = int(input("Enter the number of steps: "))
        x_vals = [a + i*(b-a)/n for i in range(n+1)]
        y_vals = [f(x) for x in x_vals]
        p = plot(expr, (x, a, b), show=False)
        p.scatter(x_vals, y_vals)
        p.show()
        return "Graph displayed."
    else:
        pass


    # Store the solution in the previous problems dictionary
    prev_problems[problem_str] = solutions

    # Return the solution(s) to the user
    return solutions

# Main loop
while True:
    # Get user input
    user_input = input("Enter a mathematical problem: ")

    # Check if the problem has already been solved
    if user_input in prev_problems:
        print(f"Result (from history): {prev_problems[user_input]}")
        continue

    # Try to solve the problem
    try:
        solutions = solve_problem(user_input)
        print(f"Result: {solutions}")
    except:
        print("Error: Could not solve the problem.")
