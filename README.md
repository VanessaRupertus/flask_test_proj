# flask_calc
This program implements a simple calculator that can only perform operations with one operand at a time (Format: number (operand) number). Any other combination will result in an ERROR message, displayed on the produced webpage.

User requests (i.e. equation) are passed to a server using POST with the Flask framework. The python script, using Flask framework, then processes the equation by identifying if only one operand exists (of either +, -, *, or /), and if yes, splits the string passed from the request and performs the operation. Then, it displays the result of the operation to the user with the option to perform another operation. If the program cannot perform the operation due to a division by zero or invalid equation string, an error message will be passed instead, with a chance to input another equation.

This project is less for the actual content (the calculator) but to understand the basics of the Flask framework and how to send and recieve data, while also incorporating html, css, some javascript, and of course, python code.
