def prefix_to_infix(expression):
    alphabet=" +-*/1234567890"
    operators="+-*/"
    numbers="1234567890"
    if any(i not in alphabet for i in expression) or not(expression) or expression[0] not in operators:
        return expression
    expr=expression.split(" ")

    operators_stack=[]
    number_stack=[]
    for symbol in expr:
        if symbol in operators:
            operators_stack.append(symbol)
        else:
            number_stack.append(symbol)
    stack=[]
    for token in reversed(expr):
        if token in operators:
            if token=="-" and len(stack)==1:
                operand=stack.pop()
                new_expr=f"- {operand}"
            elif token =="+" and len(stack)==1:
                operand=stack.pop()
                new_expr=f"{operand}"
            else:
                operand1=stack.pop()
                operand2=stack.pop()
                new_expr=f"({operand1} {token} {operand2})"
            stack.append(new_expr)
        else:
            stack.append(token)
    return stack[0]


##expressions = [
##    "+ - 13 4 55", # 13 - 4 + 55
##    "+ 2 * 2 - 2 1", # 2 + 2 * ( 2 - 1 )
##    "+ + 10 20 30", # 10 + 20 + 30
##    "- - 1 2", # - (1 - 2)
##    "/ + 3 10 * + 2 3 - 3 5" # ( 3 + 10 ) / ( 2 + 3 ) * ( 3 - 5 )
##]
##
##
##for expr in expressions:
##    infix = prefix_to_infix(expr)
##    print(f"Prefix: {expr} => Infix: {infix}")
##

