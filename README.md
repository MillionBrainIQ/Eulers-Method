# Eulers-Method
This Python program implements Euler’s Method, a simple numerical technique for approximating solutions to first-order ordinary differential equations. 
It begins by importing the math module to allow mathematical functions in the user-provided differential equation and tabulate to display results in a clean table. 
The user is prompted to enter the differential equation as a string, initial conditions x_0 and y_0, a target x value for which to approximate y, and the number of steps to take. 
The core of the program is the Euler_Method function, which calculates the step size h as the interval from the starting x to the target x divided by the number of steps. 
Within a loop that iterates for each step, the slope m at the current (x, y) is computed by evaluating the derivative string in a controlled environment using Python’s eval, allowing access to the variables x, y, and functions from math. 
The next y value is then estimated using Euler’s formula y_next = y + m * h, which linearly projects the solution along the tangent at the current point. 
The program also constructs the equation of this tangent line for visualization purposes and stores the current x, y, slope, tangent line, and next y in a table. 
After updating x and y for the next iteration, the loop continues until the final approximation is reached. 
At the end, the program prints a neatly formatted table showing all steps, slopes, tangent lines, and successive approximations, followed by the final estimated y value at the target x. 

