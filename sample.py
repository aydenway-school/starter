import math

# print("hello, this is Ayden practicing for CS210")

# i = 0

# while i < 1000:
#     print(math.sqrt(i))
#     i += 1
#     if i % 2 == 0:
#         print(f"This number {i} is even")



# based on the Leibniz formula, alternating plus and minus of 4 over a sequence of odd numbers, approximates PI

def calculatePI(iterations):
    # create new line, and then intialize code
    print()
    print("Calculating PI")
    pi = 0
    i = 1
    op = True

    # repeat for as many iterations as set
    while i < iterations:
        # The Leibniz formula alternates addition and subtraction. the op boolean tracks this alternation
        if op == True:
            pi += 4/i
        else:
            pi -= 4/i
        i += 2
        op = not op

    # this seems very stupid but I could not think of a better way off the top of my head
    # in order to show accuracy, calculate based off which number is smaller
    print(pi)
    if pi > math.pi:
        print(f"At {iterations} iterations, it achieved {math.pi / pi}% accuracy")
    if pi < math.pi:
        print(f"At {iterations} iterations, it achieved {pi / math.pi}% accuracy")

calculatePI(2)
calculatePI(100)
calculatePI(100000)
calculatePI(100000000)