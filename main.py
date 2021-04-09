
def add(v1, v2):

    print("Your Answer :-"+" "+str(v1 + v2))


def subtract(v1, v2):
    print("Your Answer :-"+" "+str(v1 - v2))


def divide(v1, v2):

    print("Your Answer :-"+" "+str(v1 * v2))


def multiply(v1, v2):

    print("Your Answer :-"+" "+str(v1 * v2))


choices = {1, 2, 3, 4}
print("For Addition Enter 1")
print("For Subtraction Enter 2")
print("For Multiplication Enter 3")
print("For Divide Enter 4")
choice = int(input("Waiting for Your Selection:-"))

if choices.__contains__(choice):
    v1 = int(input("Value 1 :- "))
    v2 = int(input("Value 2 :- "))

    if choice == 1:
        add(v1, v2)
    elif choice == 2:
        subtract(v1, v2)
    elif choice == 3:
        divide(v1, v2)
    else:
        multiply(v1, v2)

else:
    print("Enter Correct Value Please")


