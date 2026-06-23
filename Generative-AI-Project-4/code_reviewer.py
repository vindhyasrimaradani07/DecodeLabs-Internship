with open("sample_code.py", "r") as file:
    code = file.read()

print("# Intelligent Code Reviewer & Explainer")
print()

print("## INPUT CODE")
print("```python")
print(code)
print("```")

print()

print("## BUG REPORT")
print("- Division by zero error found.")
print("- Program may crash during execution.")

print()

print("## EXPLANATION")
print("The code attempts to divide a number by zero.")
print("Python does not allow division by zero, so a runtime error occurs.")

print()

print("## REFACTORED CODE")

optimized_code = """
a = 10
b = 0

if b != 0:
    print(a / b)
else:
    print("Cannot divide by zero")
"""

print("```python")
print(optimized_code)
print("```")