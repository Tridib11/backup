# try:
#     numerator=int(input("Enter a number to divide:"))
#     denominator=int(input("Enter a number to divide by:"))
#     result=numerator/denominator
# except ZeroDivisionError as e:
# # except ZeroDivisionError:
#     # print("You cant divide by zero")
#     # print(e)
# # except ValueError as e:
#     print(e)
# # except Exception:
# #     print("Something went wrong")
# # Built-in Python Exceptions
# # Here is the list of default Python exceptions with descriptions:
# # AssertionError: raised when the assert statement fails.
# # EOFError: raised when the input() function meets the end-of-file condition.
# # AttributeError: raised when the attribute assignment or reference fails.
# # TabError: raised when the indentations consist of inconsistent tabs or spaces.
# # ImportError: raised when importing the module fails.
# # IndexError: occurs when the index of a sequence is out of range
# # KeyboardInterrupt: raised when the user inputs interrupt keys (Ctrl + C or Delete).
# # RuntimeError: occurs when an error does not fall into any category.
# # NameError: raised when a variable is not found in the local or global scope.
# # MemoryError: raised when programs run out of memory.
# # ValueError: occurs when the operation or function receives an argument with the right type but the wrong value.
# # ZeroDivisionError: raised when you divide a value or variable with zero.
# # SyntaxError: raised by the parser when the Python syntax is wrong.
# # IndentationError: occurs when there is a wrong indentation.
# # SystemError: raised when the interpreter detects an internal error.
#
# else:
#     print(result)
#
# finally:
#     print("This will always execute")

a=5
b=2
k=int(input("Enter a number"))
print(k)
try:
    print("Resources open")
    print(a/b)
except Exception as e:
    print("Hey u cannot divide a number by zero",e)
finally:
    print("Resource closed")