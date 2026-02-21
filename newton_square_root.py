# Function that calculates the square root of a number using Newton's method
def newton(y, tolerance):
    if y <= 0:
        print("The number must be greater than zero.")
        return
    
    x1 = y / 2  # first approximation for the square root
    x = 0
    error = 1

    # Computes successive approximations until the error is smaller than the tolerance
    while error > tolerance:
        x = (x1 + y / x1) / 2
        error = abs(x1 - x)
        x1 = x

    return x

# Main function
def main():
    y = int(input("Enter a value to calculate its square root: "))
    tolerance = 10e-6
    root = newton(y, tolerance)
    print(f"Square root of {y}: {root:.5f}")

main()