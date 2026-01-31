import math
from tabulate import tabulate

# Create a safe evaluation environment for ODE input
allowed_names = {k: getattr(math, k) for k in dir(math) if not k.startswith("__")}

# Add some convenient shortcuts
allowed_names["pi"] = math.pi
allowed_names["e"] = math.e
allowed_names["ln"] = math.log  # Allow ln(x) as a shortcut for natural log

# Inputs
dydx = input("Enter the first order ODE:\n\t")
x_0 = float(input("\nInitial x-condition?\n\t"))
y_0 = float(input("\nInitial y-condition?\n\t"))
final = float(input("\nWhat x value are we trying to approximate?\n\t"))
steps = int(input("\nHow many steps?\n\t"))

def Euler_Method(dy_dx, x, y, final_x, s):
    h = (final_x - x) / s
    table = []

    for i in range(s):
        # Update x and y in the allowed_names dict
        allowed_names["x"] = x
        allowed_names["y"] = y

        # Safe evaluation with error handling
        try:
            m = eval(dy_dx, allowed_names)
        except Exception as e:
            print(f"Error evaluating ODE at step {i+1}: {e}")
            break

        y_next = y + m * h
        line_eq = f"y = {m}(x - {x}) + {y}"  # tangent line (just for display)

        table.append([i+1, x, y, m, line_eq, y_next])

        x += h
        y = y_next

    headers = ["Step", "x", "y", "dy/dx", "Tangent line", "y(x + h)"]
    print(tabulate(table, headers=headers, floatfmt=".5f", tablefmt="fancy_grid"))
    print("\nFinal approximation:", round(y, 6))

Euler_Method(dydx, x_0, y_0, final, steps)

