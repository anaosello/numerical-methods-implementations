# Numerical Methods Implementations

This repository contains implementations of classical numerical methods commonly used in calculus.

## Implemented Methods

### 1. Trapezoidal Rule – Approximation of π
![C++](https://img.shields.io/badge/C%2B%2B-17-blue.svg)

Approximates the value of π using the definite integral:

$$\pi = 4 \int_{0}^{1} \frac{1}{1 + x^2} \ dx$$

The integral is computed numerically using the trapezoidal rule with a user-defined number of subintervals.

---

### 2. Linear Regression – Least Squares Method
![Python](https://img.shields.io/badge/Python-3.11-blue.svg)

Computes the coefficients (a, b) of the linear equation:

$$y = ax + b$$

using the least squares method for a given set of data points.

The coefficients are calculated using the equations:

$$ a = \frac{n\sum xy - \sum x \sum y}{n\sum x^2 - (\sum x)^2}$$

$$ b = \frac{\sum y\sum x^2 - \sum x\sum xy}{n\sum x^2 - (\sum x)^2} $$

---

### 3. Square Root – Newton’s Method
![Python](https://img.shields.io/badge/Python-3.11-blue.svg)

Initial approximation:

$$X_1 = \frac{Y}{2}$$

Successive approximations:

$$X_{n+1} = \frac{1}{2}\left( X_n + \frac{n}{x_i} \right)$$

Iterations stop when the stopping criterion is satisfied:

$$\left| X_{n+1} - X_n \right| < \varepsilon$$

---

## Technologies

- Python 3
- C ++
- No external libraries required
