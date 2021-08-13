# from functions.py import *

def main(args):
    print("Use + for addition, Use - for subtraction, Use * for multiplication, Use / for division.")
    problem = input("What is the math problem to solve(one-step)? ")
    valid = False
    functions = {
        1: "+",
        2: "-",
        3: "*",
        4: "/"
    }

    for each in functions:
        if problem.contains(each):
            valid = True

    if not valid:
        print("FAIL")
        exit()

    print("PASS")

#
# class Solve:
# test
# test asus


#    def FindOperation():
