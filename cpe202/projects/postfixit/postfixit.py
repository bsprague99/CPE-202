# Name:         Brenden Sprague
# Course:       CPE 202
# Instructor:   Daniel Kauffman
# Assignment:   Postfix-It
# Term:         Winter 2021


def postfix_eval(xs: list) -> str:
    ints = []
    for x in xs:
        if number_check(x):
            ints.append(x)
        elif x in "+-/*^":
            rht = ints.pop()
            lft = ints.pop()
            ints.append(operator_finder(float(rht), float(lft), x))
    return "{:.3f}".format(float(ints.pop()))


def infix_eval(xs: list) -> list:
    stack = []
    out = []
    for x in xs:
        if number_check(x):
            out.append(x)
        elif x == "^" or x == "(":
            stack.append(x)
        elif x == ")":
            while len(stack) != 0:
                popped = stack.pop()
                if popped != "(":
                    out.append(popped)
                else:
                    break
        else:
            while len(stack) >= 1:
                if pemdas(x) > pemdas(stack[-1]):
                    break
                popped = stack.pop()
                if popped != "(" and popped != ")":
                    out.append(popped)
            stack.append(x)
    out.extend(reversed(stack))
    return out


def main() -> None:
    """
    Iteratively prompt the user for an infix expression and display both the
    postfix equivalent and, on the next line, the result as a float (even if it
    is a whole number) rounded to 3 decimal places. Assume the infix expression
    is properly formatted.
    """
    while True:

        try:
            infix = input(">>> ")
            # insert all code for main below this line

            print(" ".join(infix_eval(infix.split(" "))))

            print(postfix_eval(infix_eval(infix.split(" "))))

        except EOFError:  # loop breaks with CTRL+d
            break
    print()  # empty line prints before program ends
    # end of main (no return statement is equivalent to |return None|)


# insert additional function definitions below this line

def pemdas(operator: str) -> float:
    if operator == ")":
        return 4
    elif operator == "^":
        return 3
    elif operator == "*" or operator == "/":
        return 2
    elif operator == "+" or operator == "-":
        return 1
    return 0


def operator_finder(rht: float, lft: float, operator: str) -> float:
    if operator == "+":
        return lft + rht
    elif operator == "-":
        return lft - rht
    elif operator == "*":
        return rht * lft
    elif operator == "/":
        return lft / rht
    elif operator == "^":
        return lft ** rht
    return 0


def number_check(s: str) -> bool:
    try:
        float(s)
        return True
    except ValueError:
        return False


# do not add code below this line
if __name__ == "__main__":  # runs main with command |python3 postfixit.py|
    main()
