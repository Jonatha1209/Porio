Porio Language
===============

Porio is a simple interpreted language with basic variable declarations, assignments, conditional statements, and input/output operations.

---

1. Variable Declaration
------------------------
Variables are declared using the `val` keyword followed by the type and the variable name. By default, they are initialized with type-specific default values.

```cpp
val integer x; // x is initialized to 0
val string name; // name is initialized to ""
```

Supported Types and Default Values:
- `integer` -> `0`
- `float` -> `0.0`
- `string` -> `""`
- `bool` -> `False`

---

2. Variable Assignment
-----------------------
Variables are assigned values using the `assign` keyword.

```cpp
assign x 10;
assign name "John";
```

---

3. Output (`valLog`)
----------------------
The `valLog()` function is used to print expressions.

```cpp
valLog("Hello, World");  // Prints: Hello, World
valLog(x + 5);  // Prints the value of x + 5
```

---

4. Input (`input`)
-------------------
User input is read using the `input` keyword.

```cpp
input age integer;  // Reads an integer from user input
input username string;  // Reads a string from user input
```

---

5. Conditional Statements (`if`)
--------------------------------
Conditional statements start with `if (<condition>) {` and end with `} end`.

```cpp
if (x > 10) {
    valLog("x is greater than 10");
} end;
```

---

6. Example Code
----------------
```cpp
val integer x;
assign x 10;
valLog(x);

input y integer;
if (y > x) {
    valLog("y is greater than x");
} end;
```

---

7. Summary
-----------
- `val <type> <var>;` -> Declares a variable.
- `assign <var> <value>;` -> Assigns a value to a variable.
- `valLog(<expr>);` -> Prints an expression.
- `input <var> <type>;` -> Reads input from the user.
- `if (<condition>) { ... } end;` -> Conditional execution.
*/
