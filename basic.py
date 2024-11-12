import re
import sys 
from sys import *
from lexer_new import lex, do_print, symbols, eval_expression, getINPUT, do_assign , getVariable


#tokens = []

def open_file(filename):
    data = open(filename, "r").read()
    data += "<EOF>" 
    return data 

# Code for a simple tokenizer in basic.py


'''def parse(toks):
    i = 0
    while (i < len(toks)):
        #print(toks[i] + " " + toks[i+1])
        if toks[i] + " " + toks[i+1][0:6] == "PRINT STRING" or toks[i] + " " + toks[i+1][0:3] == "PRINT NUM" or toks[i] + " " + toks[i+1][0:4] == "PRINT EXPR" or toks[i] + " " + toks[i+1][0:3] == "PRINT VAR":
            if toks[i+1][0:6] == "STRING":
                do_print(toks[i+1])
            elif toks[i+1][0:3] == "NUM":
                do_print(toks[i+1])
            elif toks[i+1][0:4] == "EXPR":
                do_print(toks[i+1])
            elif toks[i+1][0:3] == "VAR":
                do_print(getVariable(toks[i+1]))
            i+=2
        elif toks[i][0:3] + " " + toks[i+1] + " " + toks[i+2][0:6] == "VAR EQUALS STRING" or toks[i][0:3] + " " + toks[i+1] + " " + toks[i+2][0:3] == "VAR EQUALS NUM" or toks[i][0:3] + " " + toks[i+1] + " " + toks[i+2][0:4] == "VAR EQUALS EXPR" or toks[i][0:3] + " " + toks[i+1] + " " + toks[i+2][0:3] == "VAR EQUALS VAR":
            if toks[i+2][0:6] == "STRING":
                do_assign(toks[i],toks[i+2])
            elif toks[i+2][0:3] == "NUM":
                do_assign(toks[i],toks[i+2])
            elif toks[i+2][0:4] == "EXPR":
                do_assign(toks[i],"NUM:" + str(eval_expression(toks[i+2][5:])))
            elif toks[i+2][0:3] == "VAR":
                do_assign(toks[i],getVariable(toks[i+2]))
            i+=3
        elif toks[i] + " " + toks[i+1][0:6] + " " + toks[i+2][0:3] == "INPUT STRING VAR" or toks[i] + " " + toks[i+1][0:3] + " " + toks[i+2][0:3] == "INPUT NUM VAR" or  toks[i] + " " + toks[i+1][0:4] + " " + toks[i+2][0:3] == "INPUT EXPR VAR" or  toks[i] + " " + toks[i+1][0:3] + " " + toks[i+2][0:3] == "INPUT VAR VAR":
            if toks[i+1][0:6] == "STRING":
                getINPUT(toks[i+1][7:],toks[i+2][4:])
            elif toks[i+1][0:3] == "NUM":
                getINPUT(toks[i+1][4:],toks[i+2][4:])
            elif toks[i+1][0:4] == "EXPR":
                getINPUT(toks[i+1][5:],"NUM:" + str(eval_expression(toks[i+2][5:])))
            elif toks[i+1][0:3] == "VAR":
                getINPUT(toks[i+1][4:],getVariable(toks[i+2]))
            i+=3

        elif toks[i] + " " + toks[i+1][0:6] + " " + toks[i+2][0:3] == "INPUT STRING VAR":
            getINPUT(toks[i+1][7:],toks[i+2][4:])
            i+=3'''
            
def parse(toks):
    i = 0
    while i < len(toks):
        if toks[i] == "PRINT":
            # Check if it's a complex expression
            if toks[i+1].startswith("VAR:") or toks[i+1].startswith("NUM:"):
                expr = []
                j = i + 1
                while j < len(toks) and (toks[j].startswith("VAR:") or toks[j].startswith("NUM:") or toks[j].startswith("OPERATOR")):
                    expr.append(toks[j])
                    j += 1
                # Evaluate the expression if we have more than one token
                if len(expr) > 1:
                    expr_str = " ".join([getVariable(t) if t.startswith("VAR:") else t[4:] for t in expr])
                    do_print("EXPR:" + expr_str)
                else:
                    do_print(expr[0])
                i = j
            else:
                do_print(toks[i+1])
                i += 2
        elif toks[i][0:3] + " " + toks[i+1] + " " + toks[i+2][0:6] == "VAR EQUALS STRING" or toks[i][0:3] + " " + toks[i+1] + " " + toks[i+2][0:3] == "VAR EQUALS NUM" or toks[i][0:3] + " " + toks[i+1] + " " + toks[i+2][0:4] == "VAR EQUALS EXPR" or toks[i][0:3] + " " + toks[i+1] + " " + toks[i+2][0:3] == "VAR EQUALS VAR":
            if toks[i+2][0:6] == "STRING":
                do_assign(toks[i], toks[i+2])
            elif toks[i+2][0:3] == "NUM":
                do_assign(toks[i], toks[i+2])
            elif toks[i+2][0:4] == "EXPR":
                do_assign(toks[i], "NUM:" + str(eval_expression(toks[i+2][5:])))
            elif toks[i+2][0:3] == "VAR":
                do_assign(toks[i], getVariable(toks[i+2]))
            i += 3
        elif toks[i] + " " + toks[i+1][0:6] + " " + toks[i+2][0:3] == "INPUT STRING VAR" or toks[i] + " " + toks[i+1][0:3] + " " + toks[i+2][0:3] == "INPUT NUM VAR" or  toks[i] + " " + toks[i+1][0:4] + " " + toks[i+2][0:3] == "INPUT EXPR VAR" or  toks[i] + " " + toks[i+1][0:3] + " " + toks[i+2][0:3] == "INPUT VAR VAR":
            if toks[i+1][0:6] == "STRING":
                getINPUT(toks[i+1][7:], toks[i+2][4:])
            elif toks[i+1][0:3] == "NUM":
                getINPUT(toks[i+1][4:], toks[i+2][4:])
            elif toks[i+1][0:4] == "EXPR":
                getINPUT(toks[i+1][5:], "NUM:" + str(eval_expression(toks[i+2][5:])))
            elif toks[i+1][0:3] == "VAR":
                getINPUT(toks[i+1][4:], getVariable(toks[i+2]))
            i += 3

'''def parse(toks):
    i = 0
    while i < len(toks):
        if toks[i] == "PRINT":
            expr = []
            j = i + 1
            while j < len(toks) and (toks[j].startswith("VAR:") or toks[j].startswith("NUM:") or toks[j].startswith("OPERATOR")):
                if toks[j].startswith("VAR:"):
                    expr.append(getVariable(toks[j]))
                elif toks[j].startswith("NUM:"):
                    expr.append(toks[j][4:])
                elif toks[j].startswith("OPERATOR"):
                    expr.append(toks[j][9:])
                j += 1
            
            # Join the expression tokens into a string and evaluate
            expr_str = " ".join(expr)
            do_print("EXPR:" + expr_str)
            i = j
        elif toks[i][0:3] + " " + toks[i+1] + " " + toks[i+2][0:6] == "VAR EQUALS STRING" or toks[i][0:3] + " " + toks[i+1] + " " + toks[i+2][0:3] == "VAR EQUALS NUM" or toks[i][0:3] + " " + toks[i+1] + " " + toks[i+2][0:4] == "VAR EQUALS EXPR" or toks[i][0:3] + " " + toks[i+1] + " " + toks[i+2][0:3] == "VAR EQUALS VAR":
            if toks[i+2][0:6] == "STRING":
                do_assign(toks[i], toks[i+2])
            elif toks[i+2][0:3] == "NUM":
                do_assign(toks[i], toks[i+2])
            elif toks[i+2][0:4] == "EXPR":
                do_assign(toks[i], "NUM:" + str(eval_expression(toks[i+2][5:])))
            elif toks[i+2][0:3] == "VAR":
                do_assign(toks[i], getVariable(toks[i+2]))
            i += 3
        elif toks[i] + " " + toks[i+1][0:6] + " " + toks[i+2][0:3] == "INPUT STRING VAR" or toks[i] + " " + toks[i+1][0:3] + " " + toks[i+2][0:3] == "INPUT NUM VAR" or  toks[i] + " " + toks[i+1][0:4] + " " + toks[i+2][0:3] == "INPUT EXPR VAR" or  toks[i] + " " + toks[i+1][0:3] + " " + toks[i+2][0:3] == "INPUT VAR VAR":
            if toks[i+1][0:6] == "STRING":
                getINPUT(toks[i+1][7:], toks[i+2][4:])
            elif toks[i+1][0:3] == "NUM":
                getINPUT(toks[i+1][4:], toks[i+2][4:])
            elif toks[i+1][0:4] == "EXPR":
                getINPUT(toks[i+1][5:], "NUM:" + str(eval_expression(toks[i+2][5:])))
            elif toks[i+1][0:3] == "VAR":
                getINPUT(toks[i+1][4:], getVariable(toks[i+2]))
            i += 3
''' #

'''def parse(toks):
    i = 0
    while i < len(toks):
        print(f"Parsing token at index {i}: {toks[i]}")  # Debug statement

        # Handle PRINT statements
        if toks[i] == "PRINT":
            print("Found PRINT statement")  # Debug statement
            expr = []
            j = i + 1
            while j < len(toks) and (toks[j].startswith("VAR:") or toks[j].startswith("NUM:") or toks[j].startswith("OPERATOR")):
                if toks[j].startswith("VAR:"):
                    expr.append(getVariable(toks[j]))
                elif toks[j].startswith("NUM:"):
                    expr.append(toks[j][4:])  # Extract the numeric part
                elif toks[j].startswith("OPERATOR"):
                    expr.append(toks[j][9:])  # Extract the operator
                j += 1

            expr_str = " ".join(expr)
            print("Parsed expression for PRINT:", expr_str)  # Debug output
            do_print("EXPR:" + expr_str)
            i = j

        # Handle assignment statements
        elif toks[i].startswith("VAR:") and toks[i+1] == "EQUALS":
            varname = toks[i]
            varvalue = toks[i+2]
            print(f"Assigning {varname} to {varvalue}")  # Debug output
            if varvalue.startswith("STRING"):
                do_assign(varname, varvalue)
            elif varvalue.startswith("NUM"):
                do_assign(varname, varvalue)
            elif varvalue.startswith("EXPR"):
                do_assign(varname, "NUM:" + str(eval_expression(varvalue[5:])))
            elif varvalue.startswith("VAR"):
                do_assign(varname, getVariable(varvalue))
            i += 3

        # Handle INPUT statements
        elif toks[i] == "INPUT" and toks[i+1].startswith("STRING") and toks[i+2].startswith("VAR:"):
            prompt = toks[i+1][7:-1]  # Remove quotes around prompt
            varname = toks[i+2][4:]   # Strip `VAR:` prefix
            print(f"Input prompt '{prompt}' for variable {varname}")  # Debug output
            getINPUT(prompt, varname)
            i += 3

        else:
            print(f"Unrecognized syntax at token {i}: {toks[i]}")  # Debug message for unrecognized syntax
            i += 1
'''

'''def parse(toks):
    i = 0
    while i < len(toks):
        if toks[i] == "PRINT":
            expr = []
            j = i + 1
            while j < len(toks) and (toks[j].startswith("VAR:") or toks[j].startswith("NUM:") or toks[j].startswith("OPERATOR")):
                if toks[j].startswith("VAR:"):
                    expr.append(getVariable(toks[j]))  # Retrieves "0" if variable is undefined
                elif toks[j].startswith("NUM:"):
                    expr.append(toks[j][4:])
                elif toks[j].startswith("OPERATOR"):
                    expr.append(toks[j][9:])
                j += 1
            
            expr_str = " ".join(expr)
            do_print("EXPR:" + expr_str)
            i = j
        elif toks[i].startswith("VAR") and toks[i+1] == "EQUALS":
            # Determine if the assignment involves an expression
            if toks[i+2].startswith("VAR") or toks[i+2].startswith("NUM") or toks[i+2].startswith("EXPR"):
                expr = []
                j = i + 2
                while j < len(toks) and (toks[j].startswith("VAR") or toks[j].startswith("NUM") or toks[j].startswith("OPERATOR")):
                    if toks[j].startswith("VAR"):
                        expr.append(getVariable(toks[j]))  # Use "0" if undefined
                    elif toks[j].startswith("NUM"):
                        expr.append(toks[j][4:])
                    elif toks[j].startswith("OPERATOR"):
                        expr.append(toks[j][9:])
                    j += 1
                
                expr_str = " ".join(expr)
                result = eval_expression(expr_str)  # Evaluate the full expression
                do_assign(toks[i], "NUM:" + str(result))
                i = j
            else:
                if toks[i+2].startswith("STRING"):
                    do_assign(toks[i], toks[i+2])
                elif toks[i+2].startswith("NUM"):
                    do_assign(toks[i], toks[i+2])
                elif toks[i+2].startswith("EXPR"):
                    do_assign(toks[i], "NUM:" + str(eval_expression(toks[i+2][5:])))
                i += 3
        elif toks[i] == "INPUT":
            i += 3
'''



def run():

    data = open_file(argv[1])
    toks = lex(data)
    parse(toks)

run()