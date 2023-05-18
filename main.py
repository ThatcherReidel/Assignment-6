# Python program to calculate the value of PI using the Leibniz formula

# Function to calculate the value of PI
def calculate_pi(num_iterations):
    pi = 0
    sign = 1
    denominator = 1
    
    for i in range(num_iterations):
        pi += sign * (4 / denominator)
        sign *= -1
        denominator += 2
    
    return pi

# Main function to take user input
def main():
    num_iterations = 1
    
    while True:
        try:
            num_iterations = int(input("Enter the number of iterations: "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")
    
    pi_value = calculate_pi(num_iterations)
    print("The value of PI after", num_iterations, "iterations is:", pi_value)
    
if __name__ == "__main__":
    main()

