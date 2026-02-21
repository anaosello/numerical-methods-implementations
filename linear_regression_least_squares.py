# Function to calculate the linear regression of a set of values
def regressao():
    n = int(input("Enter the number of points (x, y) that will be used to fit the line: "))

    sumx = 0
    sumy = 0
    sumxy = 0
    sumx2 = 0

    # Collecting the set of values and computing each summation contained in the formulas for coefficients a and b
    for i in range(n):
        x = float(input(f"Enter value {i+1} for x: "))
        y = float(input(f"Enter value {i+1} for y: "))
        sumx += x
        sumy += y
        sumxy += x * y
        sumx2 += x ** 2

    # Calculation of coefficients a and b
    a = ((n * sumxy) - (sumx * sumy)) / ((n * sumx2) - (sumx ** 2))
    b = ((sumy * sumx2) - (sumx * sumxy)) / ((n * sumx2) - (sumx ** 2))

    return a, b

# Main function
def main():
    a, b = regressao()
    print(f"Slope coefficient of the fitted line: a = {a}")
    print(f"Intercept of the fitted line: b = {b}")

main()