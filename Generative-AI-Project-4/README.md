# Intelligent Code Reviewer & Explainer

## Project Overview

This project is a developer utility tool that analyzes a code file, identifies bugs, explains the issue in simple language, and provides an optimized version of the code.

## Features

* Reads code from a Python file
* Detects common coding issues
* Generates a bug report
* Explains the problem in plain language
* Produces an optimized code version
* Displays output using Markdown formatting

## Technologies Used

* Python

## Project Structure

Intelligent-Code-Reviewer

* sample_code.py
* code_reviewer.py
* README.md

## Sample Input

```python
a = 10
b = 0

print(a / b)
```

## Sample Output

### Bug Report

* Division by zero error found.
* Program may crash during execution.

### Explanation

The code attempts to divide a number by zero, which causes a runtime error.

### Refactored Code

```python
a = 10
b = 0

if b != 0:
    print(a / b)
else:
    print("Cannot divide by zero")
```

## Author

Vindhya sri Maradani
DecodeLabs Generative AI Project 4
