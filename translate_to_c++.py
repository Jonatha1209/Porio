import re
import sys

class PorioToCpp:
    def __init__(self):
        self.variables = {}

    def log_error(self):
        print("LogError")

    def translate(self, code):
        lines = code.strip().split("\n")
        cpp_code = ["#include <bits/stdc++.h>", "using namespace std;", "int main() {"]
        indent = "    "
        cpp_code.append("    // Original Porio Code")
        for line in lines:
            cpp_code.append(f"    // {line}")
        cpp_code.append("")
        for line in lines:
            line = line.strip()
            cpp_line = indent
            
            if line.startswith("val "):
                parts = line.split()
                if len(parts) == 3:
                    var_type = parts[1]
                    var_name = parts[2]
                    if var_type == "integer":
                        cpp_line += f"long long {var_name} = 0;"
                    elif var_type == "float":
                        cpp_line += f"double {var_name} = 0.0;"
                    elif var_type == "string":
                        cpp_line += f"string {var_name} = \"\";"
                    elif var_type == "bool":
                        cpp_line += f"bool {var_name} = false;"
                    else:
                        self.log_error()
                else:
                    self.log_error()
            
            elif line.startswith("assign "):
                parts = line.split()
                if len(parts) == 3:
                    var_name = parts[1]
                    var_value = parts[2]
                    cpp_line += f"{var_name} = {var_value};"
                else:
                    self.log_error()
            
            elif line.startswith("valLog(") and line.endswith(")"):
                expr = line[7:-1]
                cpp_line += f"cout << {expr} << endl;"
            
            elif line.startswith("input "):
                parts = line.split()
                if len(parts) == 3:
                    var_name = parts[1]
                    var_type = parts[2]
                    if var_type in ["integer", "float", "string", "bool"]:
                        cpp_line += f"cin >> {var_name};"
                    else:
                        self.log_error()
                else:
                    self.log_error()
            
            elif line.startswith("if (") and line.endswith("{"):
                condition = line[3:-1].strip()
                cpp_line += f"if ({condition}) {{"
            
            elif line.startswith("for (") and line.endswith("{"):
                match = re.match(r"for \(assign (\w+) (\d+); (.*?); (\w+) \+= (\d+)\)", line)
                if match:
                    var_name, init_value, condition, iter_var, increment = match.groups()
                    cpp_line += f"for (int {var_name} = {init_value}; {condition}; {iter_var} += {increment}) {{"
                else:
                    self.log_error()
            
            elif line == "} end":
                cpp_code.append("}")
                continue
            
            else:
                self.log_error()
                continue
            
            cpp_code.append(cpp_line)
        
        cpp_code.append("    return 0;\n}")
        return "\n".join(cpp_code)

translator = PorioToCpp()
code = """
val integer x
input x integer
valLog(x*x)
"""

translated_code = translator.translate(code)
print(translated_code)
