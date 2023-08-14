from functions import *

def main():
    print("Use + for addition, Use - for subtraction, Use * for multiplication, Use / for division.")
    problem = input("What is the math problem to solve(one-step)? ")
    invalid = True
    functions = ["+", "-", "*", "/"]
    operator = None

    for each in functions:
        if each in problem:
            operator = each
            invalid = False

    if invalid:
        print("FAIL")
        exit()
    print("PASS")

    spaceless_problem = problem.replace(" ", "")

    integers = spaceless_problem.split(operator)
    print(integers)
    match operator:
        case "+":
            print(addition(integers))
        case "-":
            print(subtraction(integers))
        case "*":
            print(multiplication(integers))
        case "/":
            print(division(integers))
        case _:
            print("An error has occurred.")


if __name__ == '__main__':
    main()
