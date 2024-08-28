# Define the precedence of operators
precedence = {
    "^": 3,
    "*": 2,
    "/": 2,
    "+": 1,
    "-": 1,
    "(": 0
}

# Define a function to check if a character is an operand
def is_operand(c):
    return c.isalnum()

# Define a function to convert infix to prefix
def infix_to_prefix(infix):
    infix = infix[: : -1]
    # Initialize an empty stack and an empty prefix string
    stack = []
    prefix = ""

    # Loop through each character in the infix expression
    for c in infix:
        # If the character is an operand, append it to the prefix string
        if is_operand(c):
            prefix += c
        # If the character is a right parenthesis, push it to the stack
        elif c == "(":
            stack.append(c)
        # If the character is a left parenthesis, pop and append the stack until a right parenthesis is found
        elif c == ")":
            while stack and stack[-1] != "(":
                prefix += stack.pop()
            # Pop the right parenthesis from the stack
            stack.pop()
        # If the character is an operator, pop and append the stack until a lower precedence operator or a left parenthesis is found
        else:
            while stack and precedence[c] <= precedence[stack[-1]]:
                prefix += stack.pop()
            # Push the current operator to the stack
            stack.append(c)

    # Pop and append the remaining stack to the prefix string
    while stack:
        prefix += stack.pop()

    # Reverse the final prefix expression to get the correct order
    return prefix[::-1]

# Test the function with some examples
examples = ["a+b*c+d", "a-(b/c)*(a/k)-l", "a^b+c*d-e/f", "(a+b)^c*(d-e)/(f+g-h)"]
for example in examples:
    print(f"Infix: {example}")
    print(f"Prefix: {infix_to_prefix(example)}")
    print()
