import re
import sys

class PorioInterpreter:
    def __init__(self):
        self.variables = {}
        self.functions = {}

    def log_error(self):
        print("LogError")

    def eval_condition(self, condition):
        try:
            return eval(condition, {"__builtins__": {}}, self.variables)
        except:
            return False

    def eval_expression(self, expr):
        try:
            return eval(expr, {"__builtins__": {}}, self.variables)
        except:
            self.log_error()
            return 0

    def run(self, code):
        lines = code.strip().split("\n")
        i = 0
        while i < len(lines):
            line = lines[i].strip()

            if line.startswith("val "):
                parts = line.split()
                if len(parts) == 3:
                    var_type = parts[1]
                    var_name = parts[2]
                    if var_type == "integer":
                        self.variables[var_name] = 0
                    elif var_type == "float":
                        self.variables[var_name] = 0.0
                    elif var_type == "string":
                        self.variables[var_name] = ""
                    elif var_type == "bool":
                        self.variables[var_name] = False
                    else:
                        self.log_error()
                else:
                    self.log_error()

            elif line.startswith("assign "):
                parts = line.split()
                if len(parts) == 3:
                    var_name = parts[1]
                    var_value = parts[2]
                    if var_name in self.variables:
                        self.variables[var_name] = self.eval_expression(var_value)
                    else:
                        self.log_error()
                else:
                    self.log_error()

            elif line.startswith("valLog(") and line.endswith(")"):
                expr = line[7:-1]
                print(self.eval_expression(expr))

            elif line.startswith("input "):
                parts = line.split()
                if len(parts) == 3:
                    var_name = parts[1]
                    var_type = parts[2]
                    try:
                        if var_type == "integer":
                            self.variables[var_name] = int(input())
                        elif var_type == "float":
                            self.variables[var_name] = float(input())
                        elif var_type == "string":
                            self.variables[var_name] = input()
                        elif var_type == "bool":
                            self.variables[var_name] = input().lower() == "true"
                        else:
                            self.log_error()
                    except ValueError:
                        self.log_error()
                else:
                    self.log_error()

            elif line.startswith("if (") and line.endswith("{"):
                condition = line[3:-1].strip()
                if self.eval_condition(condition):
                    i += 1
                    while i < len(lines) and lines[i].strip() != "} end":
                        self.run(lines[i])
                        i += 1
                else:
                    while i < len(lines) and lines[i].strip() != "} end":
                        i += 1

            
            
            elif line == "} end":
                continue

            else:
                self.log_error()

            i += 1

interpreter = PorioInterpreter()
code = """
valLog("Hello, World")
"""

interpreter.run(code)
