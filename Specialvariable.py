"""In Python, the if __name__ == "__main__" statement is often used to define a
block of code that should only be executed when the Python script is run directly as the main program.
This means that any code inside the if block will not be executed if the script is imported as a module
into another program.The reason for using this statement is to make the code more modular and reusable.
When a Python script is imported as a module, any code in the script that is not inside the if __name__ == "__main__"
block will be executed immediately, which may not be what you want. By placing the main code block inside the if
statement, you can control when the code is executed and prevent unintended side effects when the script is imported.
In summary, the if __name__ == "__main__" statement is used to make Python code more modular and reusable, and to control
when code is executed in a script.
"""


def main():
    print("Hello\n")
    print("Welcome user")


if __name__ == "__main__":
    main()
