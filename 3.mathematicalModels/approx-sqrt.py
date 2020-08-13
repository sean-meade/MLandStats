def sqrt(x):
    # initial guess
    z = 1.0
    # Keep getting better esitmate of root 
    # of x to 2 decimal places
    while abs(z*z - x) >= 0.01:
        # Get better aprox of root
        z -= (z*z - x) / (2*z)
    return z

sqrt(8.0)