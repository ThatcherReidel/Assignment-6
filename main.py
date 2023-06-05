# Python program to calculate the value of PI using the Leibniz formula

def calculate_pi(iterations):

    pi = 0

    sign = 1

    denominator = 1



    for _ in range(iterations):

        term = 4 * sign / denominator

        pi += term

        sign *= -1

        denominator += 2



    return pi



iterations = int(input("Enter the number of iterations: "))

result = calculate_pi(iterations)

print("The value of PI:", result)