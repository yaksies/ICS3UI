from math import sqrt


def solveQuadraticEquation(a, b, c):
    discriminant = b**2 - 4 * a * c

    if discriminant < 0:
        return []

    elif discriminant == 0:
        root = (-1 * b + sqrt(discriminant)) / (2 * a)
        return [round(root, 1)]

    else:
        root1 = -1 * b + sqrt(discriminant) / (2 * a)
        root2 = -1 * b - sqrt(discriminant) / (2 * a)

        return [round(root1, 1), round(root2, 1)]


# Test cases
sol1 = solveQuadraticEquation(1, 5, 6)  # Should return [-3, -2]
sol2 = solveQuadraticEquation(2, -1, 3)  # Should return []
sol3 = solveQuadraticEquation(25, 20, 4)  # Should return [-0.4]

# Printing the results
print(sol1)
print(sol2)
print(sol3)
