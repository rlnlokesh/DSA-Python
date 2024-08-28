# Define a function to check if a character is an operator
def is_operator(c):
    return c in "+-*/^"

# Define a function to convert prefix to postfix
def prefix_to_postfix(prefix):
    # Initialize an empty stack and an empty postfix string
    stack = []
    postfix = ""
    # Loop through each character in the prefix expression in reverse order
    for c in prefix[::-1]:
        # If the character is an operator, pop two operands from the stack
        if is_operator(c):
            op1 = stack.pop()
            op2 = stack.pop()
            # Create a string by concatenating the two operands and the operator after them
            temp = op1 + op2 + c
            # Push the resultant string back to the stack
            stack.append(temp)
        # If the character is an operand, push it to the stack
        else:
            stack.append(c)
    # Pop the final string from the stack and return it as the postfix expression
    postfix+= stack.pop()
    return postfix

# Test the function with some examples
examples = ["*+AB-CD", "*-A/BC-/AKL", "+*AB*CD", "/+AB-CD"]
for example in examples:
    print(f"Prefix: {example}")
    print(f"Postfix: {prefix_to_postfix(example)}")
    print()
