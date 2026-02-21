#include <iostream>
#include <cmath>
using namespace std;

// Function to calculate the value of pi
long double integral()
{
    // Define the integration interval
    long double initial = 0.0, final = 1.0;
    double n;

    // Ask the user for the number of subintervals
    cout << "Enter the number of subintervals the interval will be divided into: ";
    cin >> n;

    // Compute the step size
    long double h = (final - initial) / n;

    // Compute the value of the integral using the trapezoidal rule
    long double sum = 0.0, x1 = initial, x2, term;
    while (x1 < final) {
        x2 = x1 + h;
        term = ((1 / (1 + pow(x1, 2))) + (1 / (1 + pow(x2, 2)))) / 2;
        sum = sum + (term * h);
        x1 = x2;
    }

    // Multiply the integral value by 4 to obtain pi
    long double pi = 4 * sum;
    return pi;
}

// Main function
int main(){
    long double pi = integral();
    cout << "Approximation for the value of pi: " << pi << endl;
    return 0;
}