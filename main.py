# from functions.py import *

def main():
    print("Use + for addition, Use - for subtraction, Use * for multiplication, Use / for division.")
    problem = input("What is the math problem to solve(one-step)? ")
    valid = False
    functions = ["+", "-", "*", "/"]

    for each in functions:
        if each in problem:
            valid = True

    if not valid:
        print("FAIL")
        exit()

    print("PASS")


if __name__ == '__main__':
    main()
