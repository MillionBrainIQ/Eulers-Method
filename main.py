import math  # Provides math functions for use in ODE expressions
from tabulate import tabulate  # Used to print results neatly in a table

# Ask user for inputs
dydx = input("\n\nWhat is the first order ODE?\n\t")  # The derivative dy/dx as a string
x_0 = float(input("\nInitial x-condition?\n\t"))  # Starting x-value
y_0 = float(input("\nInitial y-condition?\n\t"))  # Starting y-value
final = float(input("\nWhat x value are we trying to approximate?\n\t"))  # Target x-value
steps = int(input("\nHow many steps?\n\t"))  # Number of increments to reach final x

def Euler_Method(dy_dx, x, y, final_x, s):
    """
    Approximates the solution of a first-order ODE using Euler's Method.
    """
    h = (final_x - x) / s  # Step size: distance between successive x-values
    table = []  # Stores rows for the output table

    for i in range(s):
        # Evaluate the derivative at current x and y using eval
        m = eval(dy_dx, {"x": x, "y": y, "math": math})  
        
        # Calculate next y using Euler's formula
        y_next = y + m * h  
        
        # Create equation of tangent line at current point
        line_eq = f"y = {m}(x - {x}) + {y}"  
        
        # Add current step data to table
        table.append([x, y, m, line_eq, y_next])
        
        # Update x and y for next iteration
        y = y_next
        x += h

    # Table headers for clarity
    headers = ["x", "y", "dy/dx", "tangent line", "y(x + h)"]

    # Print results in a formatted table
    print(tabulate(table, headers=headers, floatfmt=".4f", tablefmt="fancy_grid"))
    
    # Print final y-approximation at target x
    print("\nFinal approximation:", round(y, 6))

# Run Euler's Method with user inputs
Euler_Method(dydx, x_0, y_0, final, steps)
