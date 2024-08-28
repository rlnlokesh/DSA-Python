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

# Define a function to convert infix to postfix
def infix_to_postfix(infix):
    # Initialize an empty stack and an empty postfix string
    stack =[]
    postfix = ""
    # Loop through each character in the infix expression
    for c in infix:
        # If the character is an operand, append it to the postfix string
        if is_operand(c):
            postfix += c
        # If the character is a left parenthesis, push it to the stack
        elif c == "(":
            stack.append(c)
        # If the character is a right parenthesis, pop and append the stack until a left parenthesis is found
        elif c == ")":
            while stack and stack[-1] != "(":
                postfix += stack.pop()
            # Pop the left parenthesis from the stack
            stack.pop()
        # If the character is an operator, pop and append the stack until a lower precedence operator or a left parenthesis is found
        else:
            while stack and precedence[c] <= precedence[stack[-1]]:
                postfix += stack.pop()
            # Push the current operator to the stack
            stack.append(c)
    # Pop and append the remaining stack to the postfix string
    while stack:
        postfix += stack.pop()
    # Return the postfix string
    return postfix

# Test the function with some examples
examples = ["a+(b*c-(d/e^f)*g)*h", "(a+b)*c", "a^b+c*d-e/f", "(a+b)^c*(d-e)/(f+g-h)"]
for example in examples:
    print(f"Infix: {example}")
    print(f"Postfix: {infix_to_postfix(example)}")
    print()
