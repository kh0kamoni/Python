for n in range(1, 101):  
    if n > 1:  # Prime numbers are greater than 1
        for i in range(2, n):
            if n % i == 0:
                break  # Not a prime, exit loop
        else:
            print(n, end=" ")  # Print prime numbers
