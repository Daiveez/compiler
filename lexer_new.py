from sys import *

tokens=[]
num_stack = {}
symbols = {}

'''def lex(filecontent):
    tok = ""
    state = 0 
    string = ""
    varstarted = 0
    var = ""
    expr = ""
    n= ""
    isexpr = 0
    filecontent = list(filecontent)
    for char in filecontent:
        tok += char
        if tok == " ":
            if state == 0:
               tok = ""
            else:
                tok= " "
        elif tok =="\n" or tok == "<EOF>":
            if expr != "" and isexpr == 1:
                tokens.append("EXPR: " + expr)
                expr = ""
            elif expr != "" and isexpr == 0:
                tokens.append("NUM: " + expr) 
                expr = ""
            elif var != "":
                tokens.append("VAR:" + var)
                var = ""
                varstarted = 0
            tok = ""
        elif tok == "=" and state == 0:
            if expr != "" and isexpr == 0:
                tokens.append("NUM: " + expr) 
                expr = ""
            if var != "":
                tokens.append("VAR:" + var)
                var = ""
                varstarted = 0
            if tokens[-1] == "EQUALS":
                tokens[-1] = "EQEQ"
            else:
                tokens.append("EQUALS")
            tok = ""
        elif tok == "!" and state == 0:
            varstarted = 1
            tok = ""  # Clear the `!` since it's just an indicator, not part of the variable name
        elif varstarted == 1:
            if tok == "<" or tok == ">":
                if var != "":
                    tokens.append("VAR:" + var)  # Add `VAR:` prefix without the `!`
                    var = ""
                    varstarted = 0
            var += tok
            tok = ""

        elif tok == "PRINT" or tok == "print":
            tokens.append("PRINT")
            tok = ""
        elif tok == "INPUT" or tok == "input":
            tokens.append("INPUT")
            tok = ""
        #elif tok == "0" or tok == "1" or tok == "2" or tok == "3" or tok == "4" or tok == "5" or tok == "6" or tok == "7" or tok == "8" or tok == "9":
         #   expr += tok
          #  tok = ""
        #elif tok in ["+", "-", "*", "/", "**", "(", ")"]:  # Check for operators
         #   if expr:  # If there's an existing number in expr, append it to tokens
          #      tokens.append("NUM: " + expr)  # Append the number token
           #     expr = ""  # Reset expr for the next number
          #  tokens.append("OPERATOR: " + tok)  # Append the operator
           # tok = ""
        elif tok.isdigit() or (tok.startswith('.') and tok[1:].isdigit()):  # Check if it's a float (e.g., .5)
            expr += tok
            tok = ""
        elif tok.replace('.', '', 1).isdigit():  # Check if the token is a float (e.g., 3.14)
            expr += tok
            tok = ""
        elif tok == "+" or tok == "-" or tok == "/" or tok == "*" or tok == "(" or tok == ")" or tok == "**":
            if expr:
                tokens.append("NUM: " + expr)
                expr = ""
            tokens.append("OPERATOR: " + tok)
            tok = ""
        elif tok == "\"" or tok == " \"":
            if state == 0:
                state = 1
            elif state == 1:
                #print("yes")
                tokens.append("STRING:" + string + "\"")
                string = ""
                state = 0
                tok = ""
        elif state == 1:
            string += tok
            tok = ""
    #print(tokens) 
    #return "" 
    return tokens
    #return filecontent
'''

def lex(filecontent):
    tok = ""
    state = 0
    string = ""
    varstarted = 0
    var = ""
    expr = ""
    isexpr = 0
    filecontent = list(filecontent)
    
    for char in filecontent:
        tok += char
        if tok == " ":
            if state == 0:
                tok = ""
            else:
                tok = " "
        elif tok == "\n" or tok == "<EOF>":
            if expr != "" and isexpr == 1:
                tokens.append("EXPR: " + expr)
                expr = ""
            elif expr != "" and isexpr == 0:
                tokens.append("NUM: " + expr)
                expr = ""
            elif var != "":
                tokens.append("VAR:" + var)
                var = ""
                varstarted = 0
            tok = ""
        elif tok == "=" and state == 0:
            if expr != "" and isexpr == 0:
                tokens.append("NUM: " + expr)
                expr = ""
            if var != "":
                tokens.append("VAR:" + var)
                var = ""
                varstarted = 0
            tokens.append("EQUALS")
            tok = ""
        elif tok == "!" and state == 0:
            varstarted = 1
            tok = ""  # Clear `!` as it’s just a marker for variable
        elif varstarted == 1:
            if tok.isalnum() or tok == "_":  # Allow variable characters
                var += tok
            else:
                tokens.append("VAR:" + var)
                var = ""
                varstarted = 0
                tok = ""
        elif tok == "PRINT" or tok == "print":
            tokens.append("PRINT")
            tok = ""
        elif tok.isdigit():
            expr += tok
            tok = ""
        elif tok in ["+", "-", "*", "/", "**"]:
            if expr:
                tokens.append("NUM: " + expr)
                expr = ""
            tokens.append("OPERATOR:" + tok)
            tok = ""
        elif tok == "\"" or tok == " \"":
            if state == 0:
                state = 1
            elif state == 1:
                tokens.append("STRING:" + string + "\"")
                string = ""
                state = 0
                tok = ""
        elif state == 1:
            string += tok
            tok = ""
    
    return tokens

def eval_expression(expr):
    return eval(expr)

'''def do_assign(varname, varvalue):
    symbols[varname[4:]] = varvalue'''
'''def eval_expression(expr_str):
    try:
        # Replace variable names (e.g., !a) with their values
        for var in symbols:
            expr_str = expr_str.replace("!" + var, str(symbols[var]))  # Replace with value

        print(f"Evaluating expression: {expr_str}")  # Debug print

        # Now evaluate the expression (e.g., 10 + 20)
        return eval(expr_str)  # Use eval to evaluate the expression
    except Exception as e:
        print(f"Error evaluating expression: {e}")
        return 0  # Return 0 if there's an error
'''

def do_assign(var_name, value):
    symbols[var_name[4:]] = value  # Store the variable in the dictionary
    print(f"Assigned {var_name[4:]} = {value}")  # Debug output

#def getVariable(varname):
 #   varname = varname[4:]
  #  if varname in symbols:
   #     return symbols[varname]
    #else:
#        return "Variable error: Undefined variable"
 #       exit()

'''def getVariable(varname):
    varname = varname[4:]  # Remove the "VAR:" prefix
    if varname in symbols:
        value = symbols[varname]
        if value.startswith("NUM:"):  # If it's a number
            return value[4:]  # Return just the number part
        elif value.startswith("STRING:"):  # If it's a string
            return value[8:-1]  # Return the string without quotes
        elif value.startswith("EXPR:"):  # If it's an expression
            return eval_expression(value[5:])  # Evaluate the expression and return the result
        else:
            return value  # Return the value directly if it's something else
    else:
        return "Variable error: Undefined variable"
'''

def getVariable(varname):
    varname = varname[4:]  # Remove the "VAR:" prefix
    if varname in symbols:
        value = symbols[varname]
        print("Retrieved", varname, "=", value)  # Debug print
        if value.startswith("NUM:"):  # If it's a number
            return value[4:]  # Return just the number part
        elif value.startswith("STRING:"):  # If it's a string
            return value[8:-1]  # Return the string without quotes
        elif value.startswith("EXPR:"):  # If it's an expression
            return eval_expression(value[5:])  # Evaluate the expression and return the result
        else:
            return value  # Return the value directly if it's something else
    else:
        print("Variable error: Undefined variable")  # Debug message
        return "Variable error: Undefined variable"


'''def getINPUT(string,varname):
    i = input(string[1:-1] + " ")
    symbols[varname] = "STRING:\""  + i + "\""
    '''
    
    
def getINPUT(prompt, varname):
    print(f"getINPUT called with prompt '{prompt}' for variable '{varname}'")  # Debug statement
    user_input = input(prompt + " ")
    try:
        if '.' in user_input:
            symbols[varname] = "NUM:" + str(float(user_input))
        else:
            symbols[varname] = "NUM:" + str(int(user_input))
    except ValueError:
        symbols[varname] = "STRING:\"" + user_input + "\""
    print("Symbols after input:", symbols)  # Debug output


def do_print(to_print):
    print(f"do_print called with argument: {to_print}")  # Debug statement
    if to_print.startswith("EXPR:"):
        result = eval_expression(to_print[5:])
    elif to_print.startswith("VAR:"):
        result = getVariable(to_print)
    elif to_print.startswith("NUM:"):
        result = to_print[4:]
    elif to_print.startswith("STRING:"):
        result = to_print[8:-1]
    else:
        result = to_print
    print("Print output:", result)




'''def do_print(to_print):
    if (to_print[0:6] == "STRING"):
        to_print = to_print[8:]
        to_print = to_print[:-1]
    elif(to_print[0:3] == "NUM"):
        to_print = to_print[4:]
    elif(to_print[0:4] == "EXPR"):
        to_print = eval_expression(to_print[5:])
    print(to_print)'''
